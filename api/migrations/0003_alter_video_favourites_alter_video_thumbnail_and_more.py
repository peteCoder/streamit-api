# Generated by Django 4.1.5 on 2020-01-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_video_favourites_alter_video_video_like_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='favourites',
            field=models.ManyToManyField(blank=True, related_name='favourites', to='api.profile'),
        ),
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(upload_to='thumbnail/'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_file',
            field=models.FileField(upload_to='videos/', verbose_name='Video file'),
        ),
    ]
