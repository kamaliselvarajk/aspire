# Generated by Django 3.2.5 on 2021-08-26 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0015_auto_20210826_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapprove',
            name='manager_name',
            field=models.CharField(default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='manager_name',
            field=models.CharField(default='1', max_length=50),
        ),
    ]
