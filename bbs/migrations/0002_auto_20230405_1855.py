# Generated by Django 3.2.15 on 2023-04-05 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collect',
            options={'managed': True, 'verbose_name': '收藏', 'verbose_name_plural': '收藏'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'managed': True, 'verbose_name': '评论', 'verbose_name_plural': '评论'},
        ),
        migrations.AlterModelOptions(
            name='follow',
            options={'managed': True, 'verbose_name': '关注', 'verbose_name_plural': '关注'},
        ),
        migrations.AlterModelOptions(
            name='like',
            options={'managed': True, 'verbose_name': '点赞', 'verbose_name_plural': '点赞'},
        ),
        migrations.AlterModelOptions(
            name='log',
            options={'managed': True, 'verbose_name': '操作日志', 'verbose_name_plural': '操作日志'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'managed': True, 'verbose_name': '消息', 'verbose_name_plural': '消息'},
        ),
        migrations.AlterModelOptions(
            name='notification',
            options={'managed': True, 'verbose_name': '系统通知', 'verbose_name_plural': '系统通知'},
        ),
        migrations.AlterModelOptions(
            name='option',
            options={'managed': True, 'verbose_name': '系统设置', 'verbose_name_plural': '系统设置'},
        ),
        migrations.AlterModelOptions(
            name='permission',
            options={'managed': True, 'verbose_name': '权限', 'verbose_name_plural': '权限'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'managed': True, 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='role',
            options={'managed': True, 'verbose_name': '角色', 'verbose_name_plural': '角色'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'managed': True, 'verbose_name': '标签', 'verbose_name_plural': '标签'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='reviewed',
            field=models.BooleanField(default=True, null=True, verbose_name='是否审核'),
        ),
        migrations.AlterField(
            model_name='log',
            name='content',
            field=models.TextField(verbose_name='内容'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='is_read',
            field=models.BooleanField(default=False, null=True, verbose_name='是否已读'),
        ),
        migrations.AlterField(
            model_name='post',
            name='read_count',
            field=models.IntegerField(default=0, null=True, verbose_name='阅读量'),
        ),
    ]
