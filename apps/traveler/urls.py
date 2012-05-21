from django.conf.urls import patterns, include, url
from traveler.views import CountryDetailView, TripDetailView, TripListView
from traveler.models import Country, Trip


urlpatterns = patterns('',  
    url(r'^country/(?P<slug>[-\w]+)/$', CountryDetailView.as_view(), name="country_detail"),
    url(r'^trips/$', TripListView.as_view(), name="trip_list_view"),
    url(r'^trips/(?P<slug>[-\w]+)/$', TripDetailView.as_view(), name="trip_detail"),
)