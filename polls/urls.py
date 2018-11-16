from . import views
#from django.conf.urls import patterns, include, url
from django.urls import include, path


app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    #path('polls/', include('polls/urls')),
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
