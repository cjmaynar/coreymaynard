from django import forms
from django.forms import ModelForm

from blog.models import Post
from blog.models import Comment

class CommentForm(ModelForm):
    post         = forms.ModelChoiceField(queryset=Post.objects.all(), widget=forms.HiddenInput())
    author       = forms.CharField(label="Your Name")
    author_url   = forms.CharField(label="Your Website", required=False)
    author_email = forms.CharField(label="Your Email", required=False)
    comment      = forms.CharField(widget=forms.Textarea())
    
    class Meta:
        model = Comment
