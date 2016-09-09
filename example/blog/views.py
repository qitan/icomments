from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except:
        print 'Err'

    return render(request,'post.html',{'post':post})
