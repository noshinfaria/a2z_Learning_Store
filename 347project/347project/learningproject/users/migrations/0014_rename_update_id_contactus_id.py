# Generated by Django 3.2.5 on 2021-09-06 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20210906_2134'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='update_id',
            new_name='id',
        ),
    ]
