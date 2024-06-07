# Generated by Django 4.2.9 on 2024-06-07 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('poster', models.ImageField(blank=True, upload_to='movie')),
                ('description', models.TextField(blank=True)),
                ('release_date', models.DateTimeField(auto_now_add=True)),
                ('actors', models.CharField(max_length=250, unique=True)),
                ('category', models.CharField(max_length=250, unique=True)),
                ('youtube_trailer_link', models.URLField()),
                ('director', models.CharField(max_length=250, unique=True)),
            ],
            options={
                'verbose_name': 'movie',
                'verbose_name_plural': 'movies',
                'ordering': ('title',),
            },
        ),
    ]
