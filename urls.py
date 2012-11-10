from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

from blog.views import HomePageView
__author__ = 'Derek Stegelman'
__date__ = '11/10/12'

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'profile/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'profile/logout.html'}, name="logout"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^traveler/', include("traveler.urls")),
    url(r'^blog/', include("blog.urls")),
    url(r'^$', HomePageView.as_view(), name="home"),
)

if settings.LOCAL:
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    urlpatterns += staticfiles_urlpatterns()