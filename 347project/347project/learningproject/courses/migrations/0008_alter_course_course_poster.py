# Generated by Django 3.2.5 on 2021-09-04 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_course_course_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_poster',
            field=models.ImageField(blank=True, default='default2.jpg', null=True, upload_to='course_posters/', verbose_name='Upload a course poster'),
        ),
    ]