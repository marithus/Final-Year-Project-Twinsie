from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Post, Comment
from .forms import CommentForm
from django.test import TestCase, RequestFactory
from .utils import is_ajax
# Testing models
class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_user.save()
        test_post = Post.objects.create(author=test_user, title='Test Post', content='This is a test post.', date_posted=timezone.now())

    def test_total_likes(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.total_likes(), 0)

    def test_total_saves(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.total_saves(), 0)

    def test_title(self):
        post = Post.objects.get(id=1)
        expected_title = f'{post.title}'
        self.assertEquals(expected_title, str(post))


class CommentModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user = User.objects.create_user(username='testuser', password='12345')
        test_user.save()
        test_post = Post.objects.create(author=test_user, title='Test Post', content='This is a test post.', date_posted=timezone.now())
        test_comment = Comment.objects.create(post=test_post, name=test_user, body='Test comment body.', date_added=timezone.now())

    def test_total_clikes(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(comment.total_clikes(), 0)

    def test_reply(self):
        comment = Comment.objects.get(id=1)
        self.assertIsNone(comment.reply)

# Testing forms
class CommentFormTest(TestCase):
    def test_comment_form_valid(self):
        form_data = {'body': 'This is a test comment.'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_comment_form_invalid(self):
        form_data = {'body': ''}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())

# Testing Utils
class IsAjaxTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def test_is_ajax(self):
        # create a regular request
        request = self.factory.get('/some/url')
        self.assertFalse(is_ajax(request)) # should return False

        # create an AJAX request
        ajax_request = self.factory.get('/some/url', HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertTrue(is_ajax(ajax_request)) # should return True
