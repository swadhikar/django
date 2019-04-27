from django import forms
from .models import Post


class CreatePostForm(forms.ModelForm):
    title = forms.CharField(required=True, max_length=100)
    content = forms.CharField(widget=forms.Textarea(attrs={'size': '60'}))

    class Meta:
        model = Post
        fields = ('title', 'content')


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')