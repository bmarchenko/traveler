from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to="images", blank=True, null=True)
    caption = models.CharField(max_length=200, blank=True, null=True)
    
    def __unicode__(self):
        return self.caption