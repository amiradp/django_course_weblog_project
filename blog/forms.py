from django import forms
from .models import UserBlogPost


class NewPostForm(forms.ModelForm):
    class Meta:
        model = UserBlogPost
        fields = ['user_title', 'user_text', 'user_author', 'user_status', 'user_email']
