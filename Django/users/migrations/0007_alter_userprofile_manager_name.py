# Generated by Django 3.2.5 on 2021-09-17 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_userprofile_manager_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='manager_name',
            field=models.CharField(choices=[('Rakesh', 'Rakesh'), ('Yasin', 'Yasin'), ('Jaya', 'Jaya'), ('Kannan', 'Kannan')], default='Kannan', max_length=50),
        ),
    ]