from django.shortcuts import render
from traveler.models import *
from django.views.generic import DetailView, ListView

class CountryDetailView(DetailView):
    
    context_object_name = "country"
    template_name = "traveler/country_detail.html"
    queryset = Country.objects.all()
    
class CountryListView(ListView):
    context_object_name = "countries"
    template_name = "traveler/country_list_view.html"
    queryset = Country.objects.all()
    paginate_by = 6
    
class TripDetailView(DetailView):
    context_object_name = "trip"
    template_name = "traveler/trip_detail.html"
    queryset = Trip.objects.all()
    
class TripListView(ListView):
    context_object_name = "trips"
    template_name = "traveler/trip_list_view.html"
    queryset = Trip.objects.all()
    paginate_by = 6
    
