from django.shortcuts import render
from .models import *

def all_post(request):
    all_post = Post.objects.all()
    context = {"all_post": all_post}

    return render(request,"myapp/all-post.html",context)

def post_detail(request,slug):
    all_post = Post.objects.all()
    post = Post.objects.get(slug = slug)

    context = {"post": post,'all_post':all_post}

    return render(request, "myapp/post-detail.html",context)