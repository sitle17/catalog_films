from django.urls import path
from .views import *
from django.views.generic import TemplateView
app_name = "films"
urlpatterns = [
    path('', index,name='main'),
    path('about/', TemplateView.as_view(template_name="about.html"), name='about'),
    path('genre/',genre_list, name='genres'),
    path('genre/<slug>/', films_in_genre, name='genre_films'),
    path('film/<int:pk>/', film_detail, name='film_detail'),
    path('film/<int:pk>/add_rewiew', create_review, name='add_review')


]

