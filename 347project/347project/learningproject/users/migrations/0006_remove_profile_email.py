# Generated by Django 3.2.5 on 2021-09-01 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_profession'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
    ]
