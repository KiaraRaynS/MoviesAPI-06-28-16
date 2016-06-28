from appmoviesapi.serializers import RaterSerializer, MovieSerializer
from django.views.generic import View
from appmoviesapi.models import Rater, Movie, MovieRating
from rest_framework import generics
import json


# Raters Views


class RatersListAPIView(generics.ListCreateAPIView):
    queryset = Rater.objects.all()
    serializer_class = RaterSerializer


class RatersDetailAPIView(generics.RetrieveAPIView):
    queryset = Rater.objects.all()
    serializer_class = RaterSerializer


class MoviesListAPIView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MoviesDetailAPIView(generics.RetrieveAPIView):
    queryset = Movie.objects.all()
    serialzer_class = MovieSerializer

"""
This was practice
class RatersListAPIView(View):

    def get(self, request):
        data_dict = list(Rater.objects.all().values())
        json_data = json.dumps(data_dict)
     return HttpResponse(json_data, content_type='application/json')
   """
