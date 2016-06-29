from rest_framework import serializers
from appmoviesapi.models import Rater, Movie, MovieRating


class RaterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rater
        fields = ('id', 'age', 'gender', 'occupation', 'zip_code')


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('id', 'release_date', 'video_release',
                  'imdb', 'unknown', 'action', 'adventure',
                  'animation', 'childrens', 'comedy', 'crime',
                  'documentary', 'drama', 'fantasy', 'film_noir',
                  'horror', 'music', 'mystery', 'romance', 'scifi',
                  'thriller', 'war', 'western'
                  )


class MovieRatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieRating
        fields = ('rater', 'movie', 'rating', 'timestamp')
