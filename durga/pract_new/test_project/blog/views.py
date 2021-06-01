from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post


posts = Post.objects.all()



def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

# class PostListView(ListView):
#     # default html page looking for  <app>/<model>_<viewtype>.html
#     # blog/post_list.html
#     model = Post
#     template_name = 'blog/home.html'
#     context_objects_name = 'posts'



def about(request):
    return render(request, 'blog/about.html', {"title": "About"})

