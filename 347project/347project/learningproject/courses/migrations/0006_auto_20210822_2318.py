# Generated by Django 3.2.5 on 2021-08-22 17:18

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20210822_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='quiz_url',
        ),
        migrations.AlterField(
            model_name='course',
            name='course_poster',
            field=models.ImageField(null=True, upload_to='course_posters', verbose_name='Upload a course poster'),
        ),
        migrations.AlterField(
            model_name='course',
            name='video',
            field=embed_video.fields.EmbedVideoField(null=True),
        ),
    ]
