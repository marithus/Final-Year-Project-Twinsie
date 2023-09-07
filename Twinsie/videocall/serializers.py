from rest_framework import serializers
from .models import RoomMember

class RoomMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomMember
        fields = '__all__'
