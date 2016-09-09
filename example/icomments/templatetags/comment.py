# -*- coding:utf8 -*-
from django import template
from django.db.models import Q
from icomments.models import Comments
from icomments.forms import ComForm


register = template.Library()

def show_comment(value):
    '''
    文章评论
    '''
    comform = ComForm()
    # 获取已批准或隐藏的评论
    comments = Comments.objects.filter(Q(approved=0)|Q(approved=3)).filter(post_id=value)
    # 构造嵌套评论
    dic={i.id:[i.id,i.parent,[],0,i] for i in comments}
    stack=[]
    for c in dic:
        i=dic[c]
        pid=i[1]
        if pid!=0 and dic.get(pid)!=None:
            p=dic[pid]
            p[2].append(i)
            i[3]=p[3]+1 
        else:
            stack.insert(0,i)
    result=[]
    while stack:
        top=stack.pop()
        result.append(top[4])
        top[2].reverse()
        stack.extend(top[2])
    comments = result

    return {'comments':comments,'comform':comform,'comment_post_id':value}

register.inclusion_tag('icomments/comment.html')(show_comment)

def show_latest_comment():
    comments = Comments.objects.filter(Q(parent=0)&Q(approved=0))[:5]

    return {'comments':comments}

register.inclusion_tag('icomments/comment_latest.html')(show_latest_comment)
