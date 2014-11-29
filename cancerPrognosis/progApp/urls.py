from django.conf.urls import patterns, include, url
from progApp import views

urlpatterns = patterns('progApp.views',
    # Examples:
    # url(r'^$', 'cancerPrognosis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^lookup/$', 'lookup', name='lookup'),
    url(r'^updatePatient/$', 'updatePatient', name='updatePatient'),
    url(r'^$', 'index', name='index'),
    url(r'^lookup/getCancerProg' ,views.getCancerProg, name = 'getCancerProg'),
)
