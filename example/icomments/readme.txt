安装

Step1:
编辑 icomments/models.py
找到 from blog.models import Post
更改为正确的文章模型

Step2:
添加 icomments 到项目
编辑 settings.py，添加
'icomments',
到INSTALLED_APPS


使用

文章详情页显示评论
eg:
{% load comment %}
<div class="comment">
{% show_comment %}
</div>

博客侧边栏最新评论
编辑 icomments/templatetags/comment_post.py
更改文章模型及各字段
编辑 icomments/templates/comment_latest.html
按实际更改文章url

然后在侧边栏位置引用以下代码
eg:
{% load comment %}
<div class="latest_comment">
{% show_latest_comment %}
</div>

