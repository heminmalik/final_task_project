from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, Review,Genre
from .forms import ReviewForm,MovieForm
from django.db.models import Q
from .forms import SearchForm
from django.contrib import messages
from .forms import GenreForm
from django.contrib.auth.models import User

# Create your views here.
def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New genre added successfully!')
            return redirect('add_genre')
    else:
        form = GenreForm()
    return render(request, 'add_genre.html', {'form': form})


def movie_list_by_genre(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    movies = genre.movies.all()
    return render(request, 'movies_by_genre.html', {'genre': genre, 'movies': movies})


def search_movies(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Movie.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))
    return render(request, 'search_results.html', {'form': form, 'query': query, 'results': results})
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('movie_detail', movie_id=movie.id)
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    reviews = movie.reviews.all()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect('login')
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user
            review.save()
            return redirect('movie_detail', movie_id=movie.id)
    else:
        form = ReviewForm()

    return render(request, 'movie_detail.html', {'movie': movie, 'reviews': reviews, 'form': form})


def addi_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Movie added successfully!')
            return redirect('addi_movie')
    else:
        form = MovieForm()
    return render(request, 'addi_movie.html', {'form': form})


def delete_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.delete()
        messages.success(request, 'Movie deleted successfully!')
        return redirect('movie_list')
    return render(request, 'delete_movie.html', {'movie': movie})


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})


def view_users(request):
    users = User.objects.all()
    return render(request, 'view_users.html', {'users': users})


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        messages.success(request, 'User deleted successfully!')
        return redirect('view_users')
    return render(request, 'delete_user.html', {'user': user})