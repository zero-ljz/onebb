from django.contrib import admin

# Register your models here.

from .models import Follow, Like, Log, Message, Notification, Option, Permission, Post, PostsTags, Role, RolesPermissions, Tag, User

admin.site.register(Follow)
admin.site.register(Like)
admin.site.register(Log)
admin.site.register(Message)
admin.site.register(Notification)
admin.site.register(Option)
admin.site.register(Permission)
admin.site.register(Post)
admin.site.register(PostsTags)
admin.site.register(Role)
admin.site.register(RolesPermissions)
admin.site.register(Tag)
admin.site.register(User)