# Generated by Django 3.2.15 on 2023-03-10 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bbs', '0015_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]