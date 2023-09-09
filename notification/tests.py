from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from feed.models import Post
from .models import Notification

class NotificationModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user2 = User.objects.create_user(username='testuser2', password='12345')
        test_post = Post.objects.create(title='test post', content='test content', author=test_user1)
        test_notification = Notification.objects.create(post=test_post, sender=test_user1, user=test_user2, notification_type=1, text_preview='test preview')

    def test_notification_str(self):
        notification = Notification.objects.get(id=1)
        expected_str = f"{notification.id} - {notification.post} - {notification.sender} - {notification.user} - {notification.notification_type}"
        self.assertEqual(expected_str, str(notification))
