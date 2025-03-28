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

class PostDetailTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='andi@sibermu.id')
        self.post = Post.objects.create(title='First post',\
                                   slug='first-post',\
                                   body='Post 1 body.',\
                                   author=self.user,\
                                   status='PB')
        self.post2 = Post.objects.create(title='Second post',\
                                   slug='second-post',\
                                   body='Post 2 body.',\
                                   author=self.user,\
                                   status='PB')

    def test_detail_post_page_returns_correct_response(self):
        response = self.client.get(f'/blog/{self.post.id}/')
        self.assertTemplateUsed(response, 'blog/post/detail.html')
        self.assertEqual(response.status_code, 200)

    def test_detail_post_page_has_correct_content(self):
        response = self.client.get(f'/blog/{self.post.id}/')
        self.assertContains(response, self.post.title)
        self.assertContains(response, self.post.body)
        self.assertNotContains(response, self.post2.title)
