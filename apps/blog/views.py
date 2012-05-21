from django.shortcuts import render
from blog.models import *
from django.views.generic import DetailView, ListView


class PostDetailView(DetailView):
    context_object_name = "post"
    template_name = "blog/post_detail_view.html"
    queryset = Post.objects.all()
    
class PostListView(ListView):
    context_object_name = "posts"
    template_name = "blog/post_list_view.html"
    queryset = Post.objects.all()
    paginate_by = 6
    
class HomePageView(ListView):
    context_object_name = "posts"
    template_name = "blog/home.html"
    queryset = Post.objects.all()
    