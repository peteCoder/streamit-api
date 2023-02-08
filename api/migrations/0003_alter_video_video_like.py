# Generated by Django 3.2.17 on 2023-02-08 07:29

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_like',
            field=models.ManyToManyField(blank=True, related_name='video_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
