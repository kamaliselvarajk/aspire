# Generated by Django 3.2.5 on 2021-09-01 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeaveApp', '0005_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaveapprove',
            name='cancel_reason',
            field=models.CharField(default='None', max_length=100),
        ),
    ]
