"""projectmoviesapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from appmoviesapi.views import IndexView
from appmoviesapi.views import RatersListAPIView, RatersDetailAPIView
from appmoviesapi.views import MoviesListAPIView, MoviesDetailAPIView, MoviesCreateAPIView
from appmoviesapi.views import MovieRatingsListAPIView, MovieRatingsDetailAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='indexview'),
    url(r'^raters/$', RatersListAPIView.as_view(), name='raterslistapiview'),
    url(r'^raters/(?P<pk>\d+)/$', RatersDetailAPIView.as_view(), name='ratersdetailview'),
    url(r'^movies/$', MoviesListAPIView.as_view(), name='movieslistapiview'),
    url(r'^movies/(?P<pk>\d+)/$', MoviesDetailAPIView.as_view(), name='moviesdetailapiview'),
    url(r'^movies/create/$', MoviesCreateAPIView.as_view(), name='moviescreateapiview'),
    url(r'^movieratings/$', MovieRatingsListAPIView.as_view(), name='movieratingslistapiview'),
    url(r'^movieratings/(?P<pk>\d+)/$', MovieRatingsDetailAPIView.as_view(), name='movieratingdetailapiview'),
]
