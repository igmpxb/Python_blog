# -*- coding: utf-8 -*-
from .models import Post
from django.shortcuts import render, get_object_or_404
def index(request):
    post_list = Post.objects.all().order_by('-creater_time')
    return render(request, 'blog/index.html',context={
                    'post_list':post_list
                  })

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/detail.html', context={'post': post})

