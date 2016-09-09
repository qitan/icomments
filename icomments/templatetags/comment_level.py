#!/usr/bin/env python
# coding=utf-8

from django import template

register = template.Library()

@register.filter(name='show_level')
def show_level(level):
    '''
    嵌套评论分级显示
    '''
    return 60*(int(level)-1)
