# Generated by Django 3.2.5 on 2021-09-04 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a2zStore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(max_length=300),
        ),
    ]