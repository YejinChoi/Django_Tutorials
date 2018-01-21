from django import forms
from .models import Post

#blog/forms.py
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__' #전체 필드
