from django.contrib import admin


# Register your models here.
from .models import Comment, Post

admin.site.register(Post)
admin.site.register(Comment)
