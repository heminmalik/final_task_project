from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.



class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    poster = models.ImageField(upload_to='movie', blank=True)
    description = models.TextField(blank=True)
    release_date=models.DateTimeField(auto_now_add=True)
    actors= models.CharField(max_length=250, unique=True)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, related_name='movies')
    category= models.CharField(max_length=250, unique=True)
    youtube_trailer_link=models.URLField()
    director=models.CharField(max_length=250, unique=True)


    class Meta:
        ordering = ('title',)
        verbose_name = 'movie'
        verbose_name_plural = 'movies'


    def __str__(self):
        return '{}'.format(self.title)


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    review_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s review of {self.movie.title}"