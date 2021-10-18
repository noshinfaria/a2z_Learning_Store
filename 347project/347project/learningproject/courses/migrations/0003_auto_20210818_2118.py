# Generated by Django 3.2.5 on 2021-08-18 15:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20210818_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='update_date',
        ),
        migrations.AlterField(
            model_name='course',
            name='publish_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
