# Generated by Django 3.2.5 on 2021-09-04 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a2zStore', '0002_alter_product_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.TextField(max_length=800),
        ),
    ]