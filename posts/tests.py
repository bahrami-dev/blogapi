from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Post

class BlogTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = 'hamed',
            email = 'hamed@bahrami.dev',
            password = 'secret'
        )

        cls.post = Post.objects.create(
            author = cls.user,
            title = 'a good title',
            body = 'a nice body content',
        )
    
    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'hamed')
        self.assertEqual(self.post.title, 'a good title')
        self.assertEqual(self.post.body, 'a nice body content')
        self.assertEqual(str(self.post), 'a good title')