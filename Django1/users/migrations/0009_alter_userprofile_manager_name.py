# Generated by Django 3.2.5 on 2021-09-19 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_userprofile_leave_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='manager_name',
            field=models.CharField(choices=[('Rakesh', 'Rakesh'), ('Yasin', 'Yasin'), ('Jaya', 'Jaya'), ('Kannan', 'Kannan')], default='None', max_length=50),
        ),
    ]
