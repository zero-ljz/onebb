from django.contrib import admin

# Register your models here.

from .models import Collect, Comment, Follow, Like, Log, Message, Notification, Option, Permission, Post, Role, Tag
from accounts.models import User

admin.site.register(Collect)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'post', 'reviewed', 'author', 'created')
    search_fields = ['content']
admin.site.register(Comment, CommentAdmin)

admin.site.register(Follow)
admin.site.register(Like)

class LogAdmin(admin.ModelAdmin):
    list_display = ('content', 'owner', 'timestamp')
admin.site.register(Log, LogAdmin)

admin.site.register(Message)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('content', 'is_read', 'timestamp')
admin.site.register(Notification, NotificationAdmin)

admin.site.register(Option)
admin.site.register(Permission)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'read_count', 'author', 'created')
    search_fields = ['title', 'content']
admin.site.register(Post, PostAdmin)

admin.site.register(Role)
admin.site.register(Tag)

class PostInline(admin.TabularInline):
    model = Post
    extra = 1

class UserAdmin(admin.ModelAdmin):
    fields = ['name','username','password','email','url','location','description','role']
    inlines = [PostInline]
    list_display = ('username', 'email', 'created')
    list_filter = ['created']
    search_fields = ['username', 'email']
    date_hierarchy = 'created'
admin.site.register(User, UserAdmin)
