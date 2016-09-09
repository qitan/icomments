# -*- coding:utf8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, verbose_name=u'作者')
    title = models.CharField(max_length=200, unique=True, verbose_name=u'标题')
    content = models.TextField(verbose_name=u'正文')
    created_date = models.DateTimeField(default=timezone.now, verbose_name=u'创建日期')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name=u'发布日期')

    def __unicode__(self):
        return self.title

