from rest_framework import serializers
from django.contrib.auth.models import User
from .models import FriendList, FriendRequest

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class FriendListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = FriendList
        fields = '__all__'

class FriendRequestSerializer(serializers.ModelSerializer):
    sender = UserSerializer()
    receiver = UserSerializer()

    class Meta:
        model = FriendRequest
        fields = '__all__'