from django import forms
from django.forms import ModelForm

from blog.models import Post
from blog.models import Comment


class CommentForm(ModelForm):
    post = forms.ModelChoiceField(queryset=Post.objects.all(), \
            widget=forms.HiddenInput())
    author = forms.CharField(label="Your Name")
    author_url = forms.CharField(label="Your Website", required=False)
    author_email = forms.CharField(label="Your Email", required=False)
    comment = forms.CharField(widget=forms.Textarea())
    extra = forms.CharField(required=False)
    math = forms.CharField(label="What's 5 + 2?")

    def clean_extra(self):
        '''If there is contents in the extra field, don't allow the comment'''
        extra = self.cleaned_data['extra']
        if extra != '':
            raise forms.ValidationError(u'Shouldn\'t be doing this...')

        return extra

    def clean_math(self):
        '''Verify that someone can do basic math'''
        math = self.cleaned_data['math']
        if int(math) != 7:
            raise forms.ValidationError(u'5 + 2 = 7')

        return math

    class Meta:
        model = Comment
        exclude = ('approved', 'admin_comment',)
