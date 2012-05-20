from django.conf.urls import patterns, include, url
from traveler.views import CountryDetailView, TripDetailView
from traveler.models import Country, Trip


urlpatterns = patterns('',  
    url(r'^country/(?P<slug>[-\w]+)/$', CountryDetailView.as_view(), name="country_detail"),
    url(r'^trip/(?P<slug>[-\w]+)/$', TripDetailView.as_view(), name="trip_detail"),
)