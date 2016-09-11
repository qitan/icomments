# -*- coding:utf8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.
APPROVED_TYPE=(
    (0,u'通过'),
    (1,u'未审核'),
    (2,u'垃圾'),
    (3,u'隐藏')
)

class Comments(models.Model):
    post_id = models.BigIntegerField(default=0,verbose_name=u'文章ID')
    author = models.CharField(max_length=100,verbose_name=u'昵称')
    author_email = models.EmailField(verbose_name=u'邮箱')
    author_url = models.CharField(max_length=200,blank=True,verbose_name=u'网址')
    author_ip = models.GenericIPAddressField(default='',blank=True, null=True,verbose_name=u'来源IP')
    date = models.DateTimeField(verbose_name=u'评论日期',default=timezone.now)
    content = models.TextField(verbose_name=u'评论内容')
    parent = models.BigIntegerField(default=0,verbose_name=u'父级评论ID')
    approved = models.IntegerField(choices=APPROVED_TYPE,default=1,verbose_name=u'评论状态')
    level = models.IntegerField(default=0,verbose_name=u'评论层级')

    def __unicode__(self):
        return self.content

    class Meta:
        ordering = ['-date']
        verbose_name = u'评论列表'
        verbose_name_plural = u'评论管理'

admin.site.register(Comments)
