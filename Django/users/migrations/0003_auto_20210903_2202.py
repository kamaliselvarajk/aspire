# Generated by Django 3.2.5 on 2021-09-03 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210903_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='username',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='password',
        ),
    ]