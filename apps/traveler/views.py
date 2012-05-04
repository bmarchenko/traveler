from django.shortcuts import render
from traveler.models import *
from django.views.generic import DetailView

class CountryDetailView(DetailView):
    
    context_object_name = "country"
    template_name = "traveler/country_detail.html"
    queryset = Country.objects.all()