from django.contrib import admin
from .models import UserBlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('user_title', 'user_author', 'user_email', 'user_datetime_modified', )


admin.site.register(UserBlogPost, BlogPostAdmin)
