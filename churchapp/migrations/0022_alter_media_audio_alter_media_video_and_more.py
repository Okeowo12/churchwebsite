# Generated by Django 4.2.5 on 2023-10-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churchapp', '0021_alter_media_audio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='uploads/audio/'),
        ),
        migrations.AlterField(
            model_name='media',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='uploads/video/'),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='sermons/audio/'),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='sermons/video/'),
        ),
    ]
