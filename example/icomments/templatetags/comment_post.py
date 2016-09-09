#!/usr/bin/env python
# coding=utf-8

from django import template
from blog.models import Post

register = template.Library()

@register.filter(name='post_id')
def post_id(value):
    '''
    显示评论文章标题
    '''
    try:
        title = Post.objects.get(pk=value).title
    except:
        print 'Err'
    return title

@register.filter(name='post_url')
def post_url(value):
    '''
    显示评论文章URL
    '''
    try:
        url = Post.objects.get(pk=value).iurl
    except:
        print 'Err'
    return url

@register.filter(name='post_category')
def post_category(value):
    '''
    显示评论文章分类
    '''
    try:
        cate = Post.objects.get(pk=value).category
    except:
        print 'Err'
    return cate
