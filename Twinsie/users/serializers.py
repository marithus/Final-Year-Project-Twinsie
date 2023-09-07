from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Relationship

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    following = UserSerializer(many=True, read_only=True)
    friends = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

class RelationshipSerializer(serializers.ModelSerializer):
    sender = ProfileSerializer()
    receiver = ProfileSerializer()

    class Meta:
        model = Relationship
        fields = '__all__'
