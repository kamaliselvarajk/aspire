# Generated by Django 3.2.5 on 2021-09-11 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeaveApp', '0017_alter_leaverequest_from_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='to_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
