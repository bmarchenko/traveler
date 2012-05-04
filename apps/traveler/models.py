from django.db import models
from django.utils import simplejson
import urllib
from hadrian.utils.slugs import unique_slugify

class Country(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    slug = models.SlugField(editable=False, max_length=120, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    latitude = models.CharField(editable=False, null=True, blank=True, max_length=120)
    longitude = models.CharField(editable=False, null=True, blank=True, max_length=120)
    
    def __unicode__(self):
        return self.name
        
    def save(self, *args, **kwargs):
        unique_slugify(self, self.name)
        location = self.name
        location = urllib.quote_plus(location)
        
        # Use google API to get silly stuff back
        google_feed = 'http://maps.googleapis.com/maps/api/geocode/json?address=' + location + '&sensor=false'
        map_data = urllib.urlopen(google_feed)
        map_json = map_data.read()
        map_object = simplejson.loads(map_json)
        result_object = map_object['results']
        location = result_object[0]['geometry']
        geos = location['location']
        self.latitude = geos['lat']
        self.longitude = geos['lng']
        super(Country, self).save(*args, **kwargs)
        
class Trip(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    slug = models.SlugField(max_length=120, editable=False)
    countries = models.ManyToManyField(Country, blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        unique_slugify(self, self.title)
        super(Trip, self).save(*args, **kwargs)