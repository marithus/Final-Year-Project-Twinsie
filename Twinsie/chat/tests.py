from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Room, Chat


class ChatModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user2 = User.objects.create_user(username='testuser2', password='12345')
        test_room = Room.objects.create(author=test_user1, friend=test_user2, created=timezone.now())
        test_chat = Chat.objects.create(room_id=test_room, author=test_user1, friend=test_user2, text='Test chat message.', date=timezone.now())

    def test_chat_str(self):
        chat = Chat.objects.get(id=1)
        expected_str = f"{chat.id} - {chat.date}"
        self.assertEqual(expected_str, str(chat))
        
        
class RoomModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        test_user1 = User.objects.create_user(username='testuser1', password='12345')
        test_user2 = User.objects.create_user(username='testuser2', password='12345')
        test_room = Room.objects.create(author=test_user1, friend=test_user2, created=timezone.now())

    def test_room_str(self):
        room = Room.objects.get(room_id=1)
        expected_str = f"{room.room_id}-{room.author}-{room.friend}"
        self.assertEqual(expected_str, str(room))