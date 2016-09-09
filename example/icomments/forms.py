# -*- coding: utf-8 -*-
from django import forms
from .models import Comments

class ComForm(forms.ModelForm):

    class Meta:
        model = Comments
        #fields = '__all__'
        fields = ('author','author_email','author_url','content')
        widgets = {
            'author': forms.TextInput(attrs={'class':'form-control col-md-7 col-xs-12','placeholder':u'昵称：','required':'required'}),
            'author_email': forms.EmailInput(attrs={'class':'form-control col-md-7 col-xs-12','placeholder':u'邮箱:','required':'required'}),
            'author_url': forms.URLInput(attrs={'class':'form-control col-md-7 col-xs-12','placeholder':u'网址:'}),
            'content': forms.Textarea(attrs={'class':'form-control col-md-7 col-xs-12','placeholder':u'评论可以一针见血...','required':'required'})
        }
