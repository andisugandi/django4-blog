from django.test import TestCase
from django.contrib.auth.models import User

from .models import Post


class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.count()
        self.assertEqual(posts, 0)

    def test_post_model_has_string_representation(self):
        user = User.objects.create(username='andi@sibermu.id')
        post = Post.objects.create(title='First post',\
                                   slug='first-post',\
                                   body='Post body.',\
                                   author=user)
        self.assertEqual(str(post), post.title)
