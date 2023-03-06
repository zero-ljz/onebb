from django.contrib import admin

# Register your models here.

from .models import Collect, Comment, Follow, Like, Log, Message, Notification, Option, Permission, Post, Role, Tag, User

admin.site.register(Collect)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Like)
admin.site.register(Log)
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(Option)
admin.site.register(Permission)
admin.site.register(Post)
admin.site.register(Role)
admin.site.register(Tag)
admin.site.register(User)