# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

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
    creater_time = models.DateTimeField(auto_now=True)
    modified_time = models.DateTimeField(auto_now=True)
    abstract = models.CharField(max_length=200,blank=True)
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User)
    def __unicode__(self):
        return self.title