from traveler.models import Trip, Country

def nav_content(request):
    context = {}
    context['international_trips'] = Trip.objects.filter(international=True)
    context['doemestic_trips'] = Trip.objects.filter(international=False)
    context['all_countries'] = Country.objects.all()
    return context