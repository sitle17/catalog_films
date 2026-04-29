from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from pytils.translit import slugify
class Genre(models.Model):
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='genre_image/', blank=True)
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)
class Films(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    year = models.DateField()
    image = models.ImageField(upload_to='film_image/',blank=True)
    rating = models.FloatField(
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)])
    genre = models.ManyToManyField(Genre)
    def __str__(self):
        return self.title

class Review(models.Model):
    STARS = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5")
    ]
    username = models.CharField(max_length=32, verbose_name='ваше имя')
    text = models.CharField(max_length=512, verbose_name='ваше мнение')
    star = models.IntegerField(choices=STARS, verbose_name='оценка')
    film = models.ForeignKey(Films, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:30]
# Create your models here.
