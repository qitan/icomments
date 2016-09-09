# -*- coding: utf8 -*-

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Q
from .models import Comments
from .forms import ComForm

# Create your views here.
def UserIP(request):
    '''
    获取评论来源IP
    '''
    if request.META.has_key('HTTP_X_FORWARDED_FOR'):
        ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        ip = request.META['REMOTE_ADDR']
    return ip

def ChildComment(action,cid,stat):
    '''
    更新或删除该评论下的回复
    action: 更新或删除操作
    cid: 该评论ID
    stat: 评论状态
    '''
    while(cid):
        cid_l = Comments.objects.filter(parent=cid)
        if cid_l:
            for i in cid_l:
                try:
                    if action == 'update':
                        Comments.objects.filter(parent=cid).update(approved=stat)
                    else:
                        Comments.objects.filter(parent=cid).delete()
                except:
                    print 'Err'

                cid = i.id
        else:
            cid = 0

#def comments(request):
#    return render(request, 'icomments/icomment.html',{})

def comments_manage(request,type=None):
    '''
    评论管理
    type: URL路由 {'list':'评论列表','trash':'垃圾评论'}
    '''
    if type == 'trash':
        comments = Comments.objects.filter(approved=2).order_by('-id')
    else:
        comments = Comments.objects.exclude(approved=2).order_by('-id')

    if request.method == 'POST':
        cid_l = request.POST.getlist('table_records')
        for cid in cid_l:
            c = get_object_or_404(Comments, pk=cid)
            if request.POST.has_key('agree'):
                c.approved = 0
                c.save()
            elif request.POST.has_key('reject'):
                c.approved = 1
                c.save()
                ChildComment('update',cid,1)
            elif request.POST.has_key('trash'):
                print 'c'
                c.approved = 2
                c.save()
                ChildComment('update',cid,2)
            elif request.POST.has_key('hidden'):
                c.approved = 3
                c.save()
            else:
                c.delete()
                ChildComment('delete',cid,2)

    return render(request, 'icomments/comment_manage.html', {'comments':comments,'type':type})

def comment_submit(request):
    comform = ComForm()
    comment = Comments()
    if request.method == 'POST':
        comform = ComForm(request.POST)
        post_id = request.POST.get('comment_post_id')
        if comform.is_valid():
            comment = comform.save(commit=False)
            comment.post_id = request.POST.get('comment_post_id')
            comment.parent = request.POST.get('comment_parent')
            # 获取评论层级
            comment.level = int(request.POST.get('comment_level')) + 1
            comment.author_ip = UserIP(request)
            r = Comments.objects.filter(Q(author=comform.cleaned_data['author'])&Q(author_email=comform.cleaned_data['author_email'])).filter(approved=0)
            # 判断用户是否存在已批准评论,如已存在，则评论无需审核
            if r:
                comment.approved = 0
            comment.save()
        else:
            print 'Err'

        post_url = reverse('post_detail', kwargs={'pk':post_id})
        return HttpResponseRedirect(post_url)


