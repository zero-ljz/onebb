# Generated by Django 3.2.15 on 2023-03-10 06:59

import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0007_auto_20230310_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, error_messages={'unique': '用户名已存在'}, help_text='要求150个字符或更少，只能是字母、数字和 @/./+/-/_。', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()]),
            preserve_default=False,
        ),
    ]
