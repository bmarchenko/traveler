from traveler.models import Trip, Country
from hadrian.contrib.locations.models import Location
def nav_content(request):
    context = {}
    context['all_trips'] = Trip.objects.all()
    context['international_trips'] = Trip.objects.filter(international=True)
    context['doemestic_trips'] = Trip.objects.filter(international=False)
    context['europe_countries'] = Country.objects.filter(continent='europe')
    context['north_america_countries'] = Country.objects.filter(continent='n-america')
    context['locations'] = Location.objects.all()
    
    return context