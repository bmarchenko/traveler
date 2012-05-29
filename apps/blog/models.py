from django.db import models
from hadrian.utils.slugs import unique_slugify
from traveler.models import Trip
from gallery.models import Image
from hadrian.contrib.locations.models import Location
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(help_text="This is automatically filled out when you save.", blank=True, null=True)
    tag_line = models.CharField(max_length=200, blank=True, null=True)
    images = models.ManyToManyField(Image, blank=True, null=True)
    location = models.ForeignKey(Location, blank=True, null=True)
    trip = models.ForeignKey(Trip, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    synopsis = models.TextField(blank=True, null=True)    
    tags = TaggableManager(blank=True)
    date_created = models.DateField(auto_now_add=False, blank=True, null=True)
    allow_comments = models.BooleanField(default=False)
    published = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        unique_slugify(self, self.title)
        super(Post, self).save(*args, **kwargs)
        
    @models.permalink
    def get_absolute_url(self):
        return ('post_detail', (), {'slug': self.slug})
        
    class Meta:
        ordering = ['-date_created']