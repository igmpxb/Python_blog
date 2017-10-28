# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Comment

# Register your models here.
class CommentsAdmin(admin.ModelAdmin):
    list_display = ['name', 'creater_time', 'text', 'post']
admin.site.register(Comment, CommentsAdmin)