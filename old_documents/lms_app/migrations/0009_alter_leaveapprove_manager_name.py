# Generated by Django 3.2.5 on 2021-08-24 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lms_app', '0008_leaverequest_no_of_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveapprove',
            name='manager_name',
            field=models.CharField(max_length=20),
        ),
    ]
