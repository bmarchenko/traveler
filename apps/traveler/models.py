from django.db import models
from django.utils import simplejson
import urllib
from hadrian.utils.slugs import unique_slugify
from hadrian.contrib.locations.models import Location
from gallery.models import Image
from traveler.choices import CONTINENT_CHOICES

class Country(models.Model):
    name = models.CharField(max_length=120, null=True, blank=True)
    slug = models.SlugField(editable=False, max_length=120, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    latitude = models.CharField(editable=False, null=True, blank=True, max_length=120)
    longitude = models.CharField(editable=False, null=True, blank=True, max_length=120)
    continent = models.CharField(max_length=50, choices=CONTINENT_CHOICES, blank=True, null=True)
    
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
        
    @models.permalink
    def get_absolute_url(self):
        return ('country_detail', (), {'slug': self.slug})
        
class Trip(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    slug = models.SlugField(max_length=120, editable=False)
    tag_line = models.CharField(max_length=200, blank=True, null=True)
    synopsis = models.TextField(blank=True, null=True)
    countries = models.ManyToManyField(Country, blank=True, null=True)
    locations = models.ManyToManyField(Location, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    images = models.ManyToManyField(Image, blank=True, null=True)
    date_left = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    date_returned = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    international = models.BooleanField(default=False)
    
    
    def __unicode__(self):
        return self.title
        
    @models.permalink
    def get_absolute_url(self):
        return ('trip_detail', (), {'slug': self.slug})
    
    def save(self, *args, **kwargs):
        unique_slugify(self, self.title)
        super(Trip, self).save(*args, **kwargs)