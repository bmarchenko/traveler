from django.contrib import admin
from traveler.models import Country, Trip

class TripAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('title', 'slug', 'international')
    search_fields = ['title', 'slug']

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'continent')
    search_fields = ['name']

admin.site.register(Country, CountryAdmin)
admin.site.register(Trip, TripAdmin)