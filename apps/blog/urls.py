from django.conf.urls import patterns, include, url
from blog.views import PostDetailView, PostListView


urlpatterns = patterns('',  
    
    url(r'^posts/$', PostListView.as_view(), name="post_list_view"),
    url(r'^posts/(?P<slug>[-\w]+)/$', PostDetailView.as_view(), name="post_detail"),
)