from django.http import HttpResponse
from .models import *
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm
from django.db.models import Avg
# Create your views here.

def film_detail(request,pk):
    film = get_object_or_404(Films, id=pk)
    form = ReviewForm()
    reviews = Review.objects.filter(film=film)
    avg_rating =reviews.aggregate(Avg('star'))
    reviews_count = reviews.count()
    context = {"film": film,
               "form": form,
               "reviews": reviews,
               "reviews_count": reviews_count,
               'avg_rating': avg_rating
               }
    return render(request, "film_detail.html", context)

def index(request):
   films = Films.objects.all()
   context = {"films": films}
   return render(request, "index.html", context)

def genre_list(request):
    genre = Genre.objects.all()
    context = {"genres": genre}
    return render(request, "genre_list.html", context)
def films_in_genre(request, slug):
    genre= get_object_or_404(Genre, slug=slug)
    films = Films.objects.filter(genre = genre)
    context = {"genre": genre, "films": films}
    return  render(request, "films_in_genre.html", context)

def create_review (request, pk):
    films = get_object_or_404(Films, id=pk )
    form = ReviewForm(request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.film = films
        review.save()

    return redirect('films:film_detail', pk)