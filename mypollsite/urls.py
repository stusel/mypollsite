#from django.conf.urls import patterns, include, url
from django.urls import include, path


from django.contrib import admin
#admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', 'mypollsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #path(r'^polls/', include('polls.urls')),
    path('polls/', include('polls.urls')),

    #path(r'^admin/', include(admin.site.urls)),
]
