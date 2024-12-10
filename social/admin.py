from django.contrib import admin
from .models import Profile, Post, Message, Comment

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Message)
admin.site.register(Comment)

