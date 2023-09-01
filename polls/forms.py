from django import forms
from .models import Poll, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Poll
        exclude = ('user', )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
