# Generated by Django 4.0 on 2022-01-08 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0007_song_duration_alter_song_cover_alter_song_lyrics'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='add_in_pl',
            field=models.BooleanField(default=False),
        ),
    ]
