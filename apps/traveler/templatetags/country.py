from django import template

register = template.Library()

__author__ = 'Derek Stegelman'
__date__ = '11/9/12'

@register.inclusion_tag('traveler/templatetags/get_country_map.html')
def get_country_map(country, height=300, width=450):
    return {'map_url': country.get_map(width, height)}