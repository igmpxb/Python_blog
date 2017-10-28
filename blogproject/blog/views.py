# -*- coding: utf-8 -*-
from .models import Post,Category
from comments.forms import CommentForm
from django.shortcuts import render, get_object_or_404
import markdown

def index(request):
    post_list = Post.objects.all().order_by('-creater_time')
    return render(request, 'blog/index.html',context={
                    'post_list':post_list
                  })

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.click_rate_add()
    post.save()

    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])

    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'blog/detail.html', context=context)

def archives(request, year, month):
    post_list = Post.objects.filter(creater_time__year=year,
                                    creater_time__month=month
                                    ).order_by('-creater_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-creater_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})
