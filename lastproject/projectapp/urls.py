from django.urls import path
from . import views
from django.contrib import admin
from .admin import admin_site

urlpatterns = [
    path('movies/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('movies/add/', views.add_movie, name='add_movie'),
    path('genres/<int:genre_id>/', views.movie_list_by_genre, name='movies_by_genre'),
    path('search/', views.search_movies, name='search_movies'),
    path('add-genre/', views.add_genre, name='add_genre'),
    path('add-movie/', views.add_movie, name='add_movie'),
    path('delete-movie/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    path('movies/', views.movie_list, name='movie_list'),
    path('view-users/', views.view_users, name='view_users'),
    path('delete-user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('admin/', admin_site.urls),

]