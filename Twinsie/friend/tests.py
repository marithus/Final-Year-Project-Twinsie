from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import FriendRequest,FriendList

class FriendRequestModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user2 = User.objects.create_user(username='testuser2', password='12345')
        test_request = FriendRequest.objects.create(sender=test_user1, receiver=test_user2, timestamp=timezone.now())

    def test_request_str(self):
        request = FriendRequest.objects.get(id=1)
        expected_str = f"{request.sender.username}"
        self.assertEqual(expected_str, str(request))

    def test_accept_request(self):
        request = FriendRequest.objects.get(id=1)
        request.accept()
        self.assertFalse(request.is_active)

    def test_decline_request(self):
        request = FriendRequest.objects.get(id=1)
        request.decline()
        self.assertFalse(request.is_active)

    def test_cancel_request(self):
        request = FriendRequest.objects.get(id=1)
        request.cancel()
        self.assertFalse(request.is_active)
        
        
    