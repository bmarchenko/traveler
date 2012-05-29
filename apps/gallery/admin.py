from django.contrib import admin
from gallery.models import Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image_preview')


admin.site.register(Image, ImageAdmin)
