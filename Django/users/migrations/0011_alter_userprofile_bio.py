# Generated by Django 3.2.5 on 2021-09-20 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_userprofile_manager_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(max_length=1000),
        ),
    ]