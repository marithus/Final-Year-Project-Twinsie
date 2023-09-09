from django.contrib import admin

# Register your models here.
from .models import Chat, Room

admin.site.register(Chat)
admin.site.register(Room)
