from django import forms
from django.forms import fields
from App_Blog.models import Comment,Blog

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)