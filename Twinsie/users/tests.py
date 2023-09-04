from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.contrib.auth.models import User
from users.models import Profile, Relationship
from friend.models import FriendList
from django.core.exceptions import ObjectDoesNotExist

class TestSignals(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='password')
        self.user2 = User.objects.create_user(username='testuser2', password='password')

    def test_create_profile_signal(self):
        profile1 = Profile.objects.get(user=self.user1)
        profile2 = Profile.objects.get(user=self.user2)
        self.assertIsNotNone(profile1)
        self.assertIsNotNone(profile2)

    def test_save_profile_signal(self):
        profile1 = Profile.objects.get(user=self.user1)
        profile1.bio = "test bio"
        profile1.save()
        updated_profile = Profile.objects.get(user=self.user1)
        self.assertEqual(updated_profile.bio, "test bio")

    def test_create_friendlist_signal(self):
        friendlist1 = FriendList.objects.get(user=self.user1)
        friendlist2 = FriendList.objects.get(user=self.user2)
        self.assertIsNotNone(friendlist1)
        self.assertIsNotNone(friendlist2)

    def test_add_to_friends_signal(self):
        Relationship.objects.create(sender=self.user1.profile, receiver=self.user2.profile, status='accepted')
        friend1 = self.user1.profile.get_friends()[0]
        friend2 = self.user2.profile.get_friends()[0]
        self.assertEqual(friend1, self.user2)
        self.assertEqual(friend2, self.user1)

    def tearDown(self):
        try:
            Profile.objects.get(user=self.user1).delete()
        except ObjectDoesNotExist:
            pass
        try:
            Profile.objects.get(user=self.user2).delete()
        except ObjectDoesNotExist:
            pass
        try:
            FriendList.objects.get(user=self.user1).delete()
        except ObjectDoesNotExist:
            pass
        try:
            FriendList.objects.get(user=self.user2).delete()
        except ObjectDoesNotExist:
            pass



