# Generated by Django 3.2.5 on 2021-08-13 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productapp', '0006_delete_userform'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('dob', models.DateField()),
            ],
        ),
    ]