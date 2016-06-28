from django.contrib import admin

from appmoviesapi.models import Rater, Movie, MovieRating

admin.site.register(Rater)
admin.site.register(Movie)
admin.site.register(MovieRating)
