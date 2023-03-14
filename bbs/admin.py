from django.contrib import admin

# Register your models here.

from .models import Collect, Comment, Follow, Like, Log, Message, Notification, Option, Permission, Post, Role, Tag
from accounts.models import User

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
