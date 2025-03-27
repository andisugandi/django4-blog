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


class PostListTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='andi@sibermu.id')
        self.post = Post.objects.create(title='First post',\
                                   slug='first-post',\
                                   body='Post body.',\
                                   author=self.user,\
                                   status='PB')

    def test_post_list_page_returns_correct_response(self):
        response = self.client.get('/blog/')
        self.assertTemplateUsed(response, 'blog/post/list.html')
        self.assertEqual(response.status_code, 200)

    def test_post_list_page_returns_correct_post_title(self):
        response = self.client.get('/blog/')
        self.assertContains(response, self.post.title)
