from django.db import models
from sorl.thumbnail import get_thumbnail

class Image(models.Model):
    image = models.ImageField(upload_to="images", blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True, null=True)
    
    def __unicode__(self):
        return self.caption
        
    def image_preview(self):
        im = get_thumbnail(self.image, "150x150")
        return '<img src="%s" width="150"/>'  % im.url
    image_preview.allow_tags = True