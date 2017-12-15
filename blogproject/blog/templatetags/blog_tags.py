from ..models import Post, Category
from django import template

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-creater_time')[:num]

@register.simple_tag
def get_top_weight_posts(num=5):
    return Post.objects.all().order_by('-top_weight','-creater_time')[:num]

@register.simple_tag
def get_click_rate_posts(num=5):
    return Post.objects.all().order_by('-click_rate')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('creater_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()


