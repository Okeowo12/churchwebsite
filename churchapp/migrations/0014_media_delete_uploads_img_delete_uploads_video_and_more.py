# Generated by Django 4.2.5 on 2023-10-09 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('churchapp', '0013_rename_audio_file_sermon_audio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clips', models.FileField(blank=True, null=True, upload_to='upload/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='upload/')),
            ],
        ),
        migrations.DeleteModel(
            name='uploads_img',
        ),
        migrations.DeleteModel(
            name='uploads_video',
        ),
        migrations.AlterField(
            model_name='sermon',
            name='audio',
            field=models.FileField(blank=True, null=True, upload_to='uploads/audio/'),
        ),
        migrations.AlterField(
            model_name='sermon',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='uploads/video/'),
        ),
    ]
