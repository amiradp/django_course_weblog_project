from django.test import TestCase
from .models import UserBlogPost
from django.contrib.auth.models import User
from django.shortcuts import reverse


class BlogPostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='user1')
        self.post = UserBlogPost.objects.create(
            user_title='post1',
            user_text='this is a test text',
            user_status=UserBlogPost.USER_STATUS_CHOICES[0][0],
            user_author=self.user,

        )

    def test_post_views_url_by_name(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_views_url(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_list_text(self):
        response = self.client.get(reverse('post_list'))
        self.assertContains(response, self.post.user_title)
