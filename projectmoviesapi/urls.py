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
from appmoviesapi.views import RatersListAPIView, RatersDetailAPIView
from appmoviesapi.views import MoviesListAPIView, MoviesDetailAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^raters/$', RatersListAPIView.as_view(), name='raterslistapiview'),
    url(r'^raters/(?P<pk>\d+)/$', RatersDetailAPIView.as_view(), name='ratersdetailview'),
    url(r'^movies/$', MoviesListAPIView.as_view(), name='movielistapiview'),
    url(r'^movies/(?P<pk>\d+)/$', MoviesDetailAPIView.as_view(), name='moviesdetailapiview')
]
