# Generated by Django 3.2.5 on 2021-09-05 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a2zStore', '0007_alter_product_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='book_url',
            field=models.URLField(default='', verbose_name='Book link'),
        ),
    ]
