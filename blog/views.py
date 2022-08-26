from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Post


# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'blog/blog.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'


class BlogCreatePostView(CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    fields = '__all__'


class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog/blog_post_edit.html'


class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete_blog_post.html'
    success_url = reverse_lazy('blog')
