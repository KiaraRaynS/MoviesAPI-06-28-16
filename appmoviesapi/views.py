from django.views.generic import TemplateView
from appmoviesapi.serializers import RaterSerializer, MovieSerializer, MovieRatingSerializer
from appmoviesapi.models import Rater, Movie, MovieRating
from rest_framework import generics


class IndexView(TemplateView):
    template_name = 'indexview.html'


# Raters Classes


class RatersListAPIView(generics.ListCreateAPIView):
    queryset = Rater.objects.all()
    serializer_class = RaterSerializer


class RatersDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rater.objects.all()
    serializer_class = RaterSerializer


# Movies Classes

class MoviesListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MoviesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serialzer_class = MovieSerializer


class MoviesCreateAPIView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# Movie Rating Classes

class MovieRatingsListAPIView(generics.ListCreateAPIView):
    queryset = MovieRating.objects.all()
    serializer_class = MovieRatingSerializer


class MovieRatingsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieRating.objects.all()
    serializer_class = MovieRatingSerializer


"""
This was practice
class RatersListAPIView(View):

    def get(self, request):
        data_dict = list(Rater.objects.all().values())
        json_data = json.dumps(data_dict)
     return HttpResponse(json_data, content_type='application/json')
   """
