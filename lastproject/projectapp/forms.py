from django import forms
from .models import Movie,Review
from .models import Genre


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'poster', 'description', 'release_date', 'actors', 'genre', 'youtube_trailer', 'director']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'review_text': forms.Textarea(attrs={'rows': 4}),
        }


class SearchForm(forms.Form):
    query = forms.CharField(label='Search for movies', max_length=100)


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']
