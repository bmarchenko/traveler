from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from blog.views import HomePageView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'profile/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'profile/logout.html'}, name="logout"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    url(r'^traveler/', include("traveler.urls")),
    url(r'^blog/', include("blog.urls")),
    url(r'^$', HomePageView.as_view(), name="home"),
)

urlpatterns += staticfiles_urlpatterns()