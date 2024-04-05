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
from django.urls import reverse

class Collect(models.Model):
    collector = models.ForeignKey('accounts.User', models.CASCADE)
    collected = models.ForeignKey('Post', models.CASCADE)
    timestamp = models.DateTimeField(blank=False, null=True, auto_now_add=True)

    def __str__(self):
        return self.collector.name + ' 收藏了文章：' + self.collected.title

    class Meta:
        managed = True
        db_table = 'collect'
        verbose_name_plural = '收藏'
        verbose_name = '收藏'


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField('评论内容', blank=False, null=True)
    created = models.DateTimeField(blank=False, null=True, auto_now_add=True)
    reviewed = models.BooleanField('是否审核', blank=False, null=True, default=True)
    post = models.ForeignKey('Post', models.CASCADE, blank=False, null=True)
    author = models.ForeignKey('accounts.User', models.CASCADE, blank=False, null=True)
    replied = models.ForeignKey('self', models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.content
    
    class Meta:
        managed = True
        db_table = 'comment'
        verbose_name_plural = '评论'
        verbose_name = '评论'


class Follow(models.Model):
    follower = models.ForeignKey('accounts.User', models.CASCADE, related_name='follower_user')
    followed = models.ForeignKey('accounts.User', models.CASCADE, related_name='followed_user')
    timestamp = models.DateTimeField(blank=False, null=True, auto_now_add=True)

    def __str__(self):
        return self.follower.name + ' 关注了 ' + self.followed.name

    class Meta:
        managed = True
        db_table = 'follow'
        verbose_name_plural = '关注'
        verbose_name = '关注'


class Like(models.Model):
    liker = models.ForeignKey('accounts.User', models.CASCADE)
    liked = models.ForeignKey('Post', models.CASCADE)
    timestamp = models.DateTimeField(blank=False, null=True, auto_now_add=True)

    def __str__(self):
        return self.liker.name + ' 点赞了文章：' + self.liked.title

    class Meta:
        managed = True
        db_table = 'like'
        verbose_name_plural = '点赞'
        verbose_name = '点赞'


class Log(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField('内容')
    timestamp = models.DateTimeField(blank=False, null=True, auto_now_add=True)
    owner = models.ForeignKey('accounts.User', models.CASCADE, blank=False, null=True)

    def __str__(self):
        return self.content
    
    class Meta:
        managed = True
        db_table = 'log'
        verbose_name_plural = '操作日志'
        verbose_name = '操作日志'


class Message(models.Model):
    sender = models.ForeignKey('accounts.User', models.CASCADE, related_name='sender_user')
    received = models.ForeignKey('accounts.User', models.CASCADE, related_name='received_user')
    content = models.TextField('消息内容', blank=False, null=True)
    timestamp = models.DateTimeField(blank=False, null=True, auto_now_add=True)

    def __str__(self):
        return self.sender.name + ' 对 ' + self.received.name + ' 说：' + self.content
    
    class Meta:
        managed = True
        db_table = 'message'
        verbose_name_plural = '消息'
        verbose_name = '消息'


class Notification(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField('通知内容')
    is_read = models.BooleanField('是否已读', blank=False, null=True, default=False)
    timestamp = models.DateTimeField(blank=False, null=True, auto_now_add=True)
    receiver = models.ForeignKey('accounts.User', models.CASCADE, blank=False, null=True)

    def __str__(self):
        return self.content
    
    class Meta:
        managed = True
        db_table = 'notification'
        verbose_name_plural = '系统通知'
        verbose_name = '系统通知'


class Option(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('名称', blank=False, null=True, max_length=200)
    value = models.TextField('值', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'option'
        verbose_name_plural = '系统设置'
        verbose_name = '系统设置'


class Permission(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=True, max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'permission'
        verbose_name_plural = '权限'
        verbose_name = '权限'


class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=True, unique=True, max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'tag'
        verbose_name_plural = '标签'
        verbose_name = '标签'


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('标题', blank=False, null=True, max_length=200)
    content = models.TextField('内容', blank=False, null=True)
    content_html = models.TextField(blank=True, null=True)
    read_count = models.IntegerField('阅读量', blank=False, null=True, default=0)
    created = models.DateTimeField(blank=False, null=True, auto_now_add=True) # default=timezone.now
    author = models.ForeignKey('accounts.User', models.CASCADE, blank=False, null=True)
    
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('bbs:post-detail', kwargs={'pk': self.pk})
    
    class Meta:
        managed = True
        db_table = 'post'
        verbose_name_plural = '文章'
        verbose_name = '文章'


class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(blank=False, null=True, max_length=200)

    permissions = models.ManyToManyField(Permission, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        managed = True
        db_table = 'role'
        verbose_name_plural = '角色'
        verbose_name = '角色'

from django.utils import timezone
from django.contrib.auth.models import PermissionsMixin

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



    # from django.contrib.auth.validators import UnicodeUsernameValidator

    # username_validator = UnicodeUsernameValidator()
    # username = models.CharField(max_length=150, unique=True, help_text='要求150个字符或更少，只能是字母、数字和 @/./+/-/_。', validators=[username_validator],
    #     error_messages={
    #         'unique': "用户名已存在",
    #     },
    # )
    # first_name = models.CharField(max_length=150, blank=True)
    # last_name = models.CharField(max_length=150, blank=True)
    # email = models.EmailField(blank=True)
    # is_staff = models.BooleanField(default=False) # 指定用户是否可以登录到此管理站点。
    # is_active = models.BooleanField(default=True) # 1、指定是否应将此用户视为活动用户。 2、取消选择而不是删除帐户。

    # date_joined = models.DateTimeField(default=timezone.now)

    # objects = UserManager()

    # EMAIL_FIELD = 'email'
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = ['email']


