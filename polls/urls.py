from . import views
#from django.conf.urls import patterns, include, url
from django.urls import include, path


urlpatterns = [
    path('', views.index, name='index'),
]
