from django.db import models


# Create your models here.

from django.contrib.auth.models import AbstractUser, UserManager
class User(AbstractUser):
    id = models.AutoField(primary_key=True)
    name = models.CharField('名字', blank=True, null=True, max_length=200)
    password = models.CharField('密码',blank=True, null=True, max_length=200)
    url = models.URLField('个人主页',blank=True, null=True, max_length=200)
    location = models.CharField('所在位置',blank=True, null=True, max_length=200, default='火星')
    description = models.CharField('个人描述',blank=True, null=True, max_length=200, default='没有个人描述')
    last_login = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField('注册时间', blank=False, null=True, auto_now_add=True)
    role = models.ForeignKey('bbs.Role', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.username
    
        
    class Meta:
        managed = True
        db_table = 'user'
        verbose_name_plural = '用户'
        verbose_name = '用户'