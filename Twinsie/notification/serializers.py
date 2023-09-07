from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Notification

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class NotificationSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(required=False)
    sender = UserSerializer()
    user = UserSerializer()

    class Meta:
        model = Notification
        fields = ['post', 'notification_type', 'text_preview', 'date', 'is_seen']
