from django.conf.urls import patterns, include, url
from traveler.views import CountryDetailView
from traveler.models import Country


urlpatterns = patterns('',  
    url(r'^country/(?P<slug>[-\w]+)/$', CountryDetailView.as_view(), name="country_detail"),
)