# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.html import strip_tags
import markdown
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
class Tag(models.Model):
    name = models.CharField(max_length=100)
    def __unicode__(self):
        return self.name
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    creater_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    abstract = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    click_rate = models.IntegerField(default=0)
    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    def click_rate_add(self):
        self.click_rate=self.click_rate+1
    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.abstract:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.abstract = strip_tags(md.convert(self.body))[:54]

        # 调用父类的 save 方法将数据保存到数据库中
        super(Post, self).save(*args, **kwargs)