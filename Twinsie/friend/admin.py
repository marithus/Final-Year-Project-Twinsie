from django.contrib import admin

# Register your models here.
from friend.models import FriendList, FriendRequest

admin.site.register(FriendList)
admin.site.register(FriendRequest)
