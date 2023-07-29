from django.db import models
from django.shortcuts import reverse


class UserBlogPost(models.Model):
    USER_STATUS_CHOICES = (
        ('pub', 'Published'),
        ('drf', 'Draft'),
    )

    user_title = models.CharField(max_length=100)
    user_text = models.TextField()
    user_author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    user_date_created = models.DateTimeField(auto_now_add=True)
    user_datetime_modified = models.DateTimeField(auto_now=True)
    user_status = models.CharField(choices=USER_STATUS_CHOICES, max_length=3)
    user_email = models.EmailField(max_length=50)

    def __str__(self):
        return f'post title : {self.user_title}/ author : {self.user_author}'

    def get_absolute_url(self):
        return reverse('detail_views', args=[self.id])
