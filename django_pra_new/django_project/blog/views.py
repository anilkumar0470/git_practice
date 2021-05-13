from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.

posts = [
    {
        "author" : "anil",
        "title": "blog post1",
        "content": "our first post content",
        "date": "26/3/2021"},
    {
        "author": "kumar",
        "title": "blog post2",
        "content": "our second post conte",
        "date": "27/3/2021"

    }
]


def home(request):

    context = {
        'posts': Post.objects.all()
    }

    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
