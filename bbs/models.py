# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

# 这是一个自动生成的Django模型模块。
# 你必须手动执行以下操作来清理:
# *重新排列模型的顺序
# *确保每个模型都有一个字段primary_key=True
# *确保每个ForeignKey和OneToOneField都有“on_delete”设置为所需的行为
# *如果你想让Django创建，修改和删除表，删除' managed = True '行
# 可以重命名模型，但不要重命名db_table的值或字段名。

from django.db import models


class Collect(models.Model):
    collector = models.ForeignKey('User', models.CASCADE)
    collected = models.ForeignKey('Post', models.CASCADE)
    timestamp = models.DateTimeField(blank=False, null=True, auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'collect'


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(blank=False, null=True)
    created = models.DateTimeField(blank=False, null=True, auto_now_add=True)
    reviewed = models.BooleanField(blank=False, null=True, default=True)
    post = models.ForeignKey('Post', models.CASCADE, blank=False, null=True)
    author = models.ForeignKey('User', models.CASCADE, blank=False, null=True)
    replied = models.ForeignKey('self', models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.content
    
    class Meta:
        managed = True
        db_table = 'comment'


class Follow(models.Model):
    follower = models.ForeignKey('User', models.CASCADE, related_name='follower_user')
    followed = models.ForeignKey('User', models.CASCADE, related_name='followed_user')
    timestamp = models.DateTimeField(blank=False, null=True, auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'follow'


class Like(models.Model):
    liker = models.ForeignKey('User', models.CASCADE)
    liked = models.ForeignKey('Post', models.CASCADE)
    timestamp = models.DateTimeField(blank=False, null=True, auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'like'


class Log(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    timestamp = models.DateTimeField(blank=False, null=True, auto_now_add=True)
    owner = models.ForeignKey('User', models.CASCADE, blank=False, null=True)

    def __str__(self):
        return self.content
    
    class Meta:
        managed = True
        db_table = 'log'


class Message(models.Model):
    sender = models.ForeignKey('User', models.CASCADE, related_name='sender_user')
    received = models.ForeignKey('User', models.CASCADE, related_name='received_user')
    content = models.TextField(blank=False, null=True)
    timestamp = models.DateTimeField(blank=False, null=True, auto_now_add=True)

    def __str__(self):
        return self.content
    
    class Meta:
        managed = True
        db_table = 'message'


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    is_read = models.BooleanField(blank=False, null=True, default=False)
    timestamp = models.DateTimeField(blank=False, null=True, auto_now_add=True)
    receiver = models.ForeignKey('User', models.CASCADE, blank=False, null=True)

    def __str__(self):
        return self.content
    
    class Meta:
        managed = True
        db_table = 'notification'


class Option(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=True, max_length=200)
    value = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'option'


class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=True, max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'permission'


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=True, unique=True, max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'tag'


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(blank=False, null=True, max_length=200)
    content = models.TextField(blank=False, null=True)
    content_html = models.TextField(blank=True, null=True)
    read_count = models.IntegerField(blank=False, null=True, default=0)
    created = models.DateTimeField(blank=False, null=True, auto_now_add=True) # default=timezone.now
    author = models.ForeignKey('User', models.CASCADE, blank=False, null=True)
    
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
    
    class Meta:
        managed = True
        db_table = 'post'


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=True, max_length=200)

    permissions = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'role'


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=True, null=True, max_length=200)
    username = models.CharField(blank=False, unique=True, null=True, max_length=200)
    password = models.CharField(blank=True, null=True, max_length=200)
    mail = models.EmailField(blank=True, unique=True, null=True, max_length=200)
    url = models.URLField(blank=True, null=True, max_length=200)
    location = models.CharField(blank=True, null=True, max_length=200)
    description = models.CharField(blank=True, null=True, max_length=200)
    last_login = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(blank=False, null=True, auto_now_add=True)
    role = models.ForeignKey(Role, models.DO_NOTHING, blank=True, null=True)
    
    def __str__(self):
        return self.username
    
    def create(self):
        pass
    def save(self):
        pass
    def delete(self):
        pass
    def set_password(self):
        pass
    def check_password(self):
        pass
        
    class Meta:
        managed = True
        db_table = 'user'
