from django.db import models
from hadrian.utils.slugs import unique_slugify
from gallery.models import Image
from hadrian.contrib.locations.models import Location

class Post(models.Model):
    title = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(editable=False, blank=True, null=True)
    images = models.ManyToManyField(Image, blank=True, null=True)
    location = models.ForeignKey(Location, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    synopsis = models.TextField(blank=True, null=True)    
    date_created = models.DateField(auto_now_add=True, blank=True, null=True)
    
    
    def __unicode__(self):
        return self.title
        
    def save(self, *args, **kwargs):
        unique_slugify(self, self.title)
        super(Post, self).save(*args, **kwargs)
        
    @models.permalink
    def get_absolute_url(self):
        return ('post_detail', (), {'slug': self.slug})