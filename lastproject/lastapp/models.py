from django.db import models

# Create your models here.
class Category(models.Model):
    movie_name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    image=models.ImageField(upload_to='category',blank=True)


    class Meta:
        ordering=('movie_name',)
        verbose_name='category'
        verbose_name_plural='categories'


    def __str__(self):
        return '{}' .format(self.name)


class Movie(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='movie', blank=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'




    def __str__(self):
        return '{}'.format(self.name)
