# Generated by Django 3.2.5 on 2021-09-07 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile_domain'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='group',
            field=models.CharField(choices=[('Employee', 'Employee'), ('Manager', 'Manager')], default='Admin', max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='domain',
            field=models.CharField(default='Python', max_length=30),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=20),
        ),
    ]
