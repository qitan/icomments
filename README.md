# icomments
Django嵌套评论-icomments

嵌套评论基于https://github.com/evilbinary/myblog.git  

###安装

Step1:

    git clone https://github.com/qitan/icomments.git

Step2:

编辑 icomments/models.py  
找到 from blog.models import Post  
更改为项目文章模型

Step3:

添加 icomments 到项目  
编辑 settings.py，添加

    'icomments',
    
到INSTALLED_APPS

Step4:

编辑 urls.py, 添加路由

    url(r'', include('icomments.urls')),

Step5:

同步数据库

    python manage.py makemigrations
    python manage.py migrate


###使用

#####文章详情页显示评论  

    {% load comment %}  
    <div class="comment">  
    {% show_comment %}  
    </div>

#####博客侧边栏最新评论  
编辑 icomments/templatetags/comment_post.py    
更改文章模型及各字段

编辑 icomments/templates/comment_latest.html  
按实际更改文章url

然后在侧边栏位置引用以下代码  


    {% load comment %}  
    <div class="latest_comment">  
    {% show_latest_comment %}  
    </div>
