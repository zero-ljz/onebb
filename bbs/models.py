# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Collect(models.Model):
    collector = models.ForeignKey('User', models.DO_NOTHING)
    collected = models.ForeignKey('Post', models.DO_NOTHING)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'collect'


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    reviewed = models.BooleanField(blank=True, null=True)
    post = models.ForeignKey('Post', models.DO_NOTHING, blank=True, null=True)
    author = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    replied = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'comment'


class Follow(models.Model):
    follower = models.ForeignKey('User', models.DO_NOTHING, related_name='follower_user')
    followed = models.ForeignKey('User', models.DO_NOTHING, related_name='followed_user')
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'follow'


class Like(models.Model):
    liker = models.ForeignKey('User', models.DO_NOTHING)
    liked = models.ForeignKey('Post', models.DO_NOTHING)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'like'


class Log(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    timestamp = models.DateTimeField(blank=True, null=True)
    owner = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'log'


class Message(models.Model):
    sender = models.ForeignKey('User', models.DO_NOTHING, related_name='sender_user')
    received = models.ForeignKey('User', models.DO_NOTHING, related_name='received_user')
    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'message'


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    is_read = models.BooleanField(blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    receiver = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'notification'


class Option(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=200)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'option'


class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=200)

    class Meta:
        managed = True
        db_table = 'permission'


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=True, null=True, max_length=200)
    content = models.TextField(blank=True, null=True)
    content_html = models.TextField(blank=True, null=True)
    read_count = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'post'


class PostsTags(models.Model):
    post = models.ForeignKey(Post, models.DO_NOTHING, blank=True, null=True)
    tag = models.ForeignKey('Tag', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'posts_tags'


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=200)

    class Meta:
        managed = True
        db_table = 'role'


class RolesPermissions(models.Model):
    role = models.ForeignKey(Role, models.DO_NOTHING, blank=True, null=True)
    permission = models.ForeignKey(Permission, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'roles_permissions'


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=200)

    class Meta:
        managed = True
        db_table = 'tag'


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=200)
    username = models.CharField(blank=True, null=True, max_length=200)
    password = models.CharField(blank=True, null=True, max_length=200)
    mail = models.CharField(blank=True, null=True, max_length=200)
    url = models.CharField(blank=True, null=True, max_length=200)
    location = models.CharField(blank=True, null=True, max_length=200)
    description = models.CharField(blank=True, null=True, max_length=200)
    last_login = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    role = models.ForeignKey(Role, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'user'
