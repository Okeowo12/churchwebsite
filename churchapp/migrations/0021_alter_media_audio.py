# Generated by Django 4.2.5 on 2023-10-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churchapp', '0020_alter_media_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
