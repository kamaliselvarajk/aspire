# Generated by Django 3.2.5 on 2021-09-02 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LeaveApp', '0013_auto_20210902_1247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaverequest',
            name='from_date',
        ),
        migrations.RemoveField(
            model_name='leaverequest',
            name='to_date',
        ),
    ]
