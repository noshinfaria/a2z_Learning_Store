# Generated by Django 3.2.5 on 2021-08-18 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20210818_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
