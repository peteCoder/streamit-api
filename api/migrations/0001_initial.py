# Generated by Django 3.2.17 on 2023-02-09 04:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField(max_length=500)),
                ('image', models.ImageField(null=True, upload_to='profile/actors/')),
            ],
            options={
                'verbose_name': 'Actor',
                'verbose_name_plural': 'Actors',
            },
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('bio', models.TextField(blank=True, max_length=500, null=True)),
                ('image', models.ImageField(null=True, upload_to='profile/director/')),
            ],
            options={
                'verbose_name': 'Director',
                'verbose_name_plural': 'Directors',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
            ],
            options={
                'verbose_name': 'Mood',
                'verbose_name_plural': 'Moods',
            },
        ),
        migrations.CreateModel(
            name='PlayList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'Playlist',
                'verbose_name_plural': 'Playlists',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=40)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='media/profile/')),
                ('bio', models.TextField(blank=True, help_text='Enter not more than 200 words.. ', max_length=200, verbose_name='User bio')),
                ('country', models.CharField(blank=True, max_length=100)),
                ('gender', models.CharField(blank=True, max_length=30)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'User Profiles',
            },
        ),
        migrations.CreateModel(
            name='VideoCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
            options={
                'verbose_name': 'Video Category',
                'verbose_name_plural': 'Video Categories',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('age_rating', models.IntegerField()),
                ('desktop_thumbnail', models.ImageField(upload_to='thumbnail/')),
                ('mobile_thumbnail', models.ImageField(upload_to='thumbnail/')),
                ('mobile_banner', models.ImageField(upload_to='banner/')),
                ('desktop_banner', models.ImageField(upload_to='banner/')),
                ('video_link', models.URLField(max_length=300, null=True)),
                ('description', models.CharField(blank=True, max_length=150, null=True)),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=False)),
                ('_actors', models.ManyToManyField(blank=True, related_name='actor_videos', to='api.Actor')),
                ('_genres', models.ManyToManyField(blank=True, related_name='genres_videos', to='api.Genre')),
                ('_moods', models.ManyToManyField(blank=True, related_name='videos', to='api.Mood')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos_uploaded', to='api.profile')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='api.videocategory')),
                ('director', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_directed', to='api.director')),
                ('favourites', models.ManyToManyField(blank=True, related_name='favourites', to='api.Profile')),
                ('playlist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videos', to='api.playlist')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
    ]
