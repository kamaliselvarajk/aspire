# Generated by Django 3.2.5 on 2021-08-27 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LeaveApp', '0002_leaveapprove'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leaveapprove',
            old_name='emp_name',
            new_name='emp_name_id',
        ),
    ]