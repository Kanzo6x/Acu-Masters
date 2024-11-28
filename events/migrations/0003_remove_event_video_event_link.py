# Generated by Django 5.1.2 on 2024-11-28 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_eventphoto_alter_event_cover_photo_alter_event_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='video',
        ),
        migrations.AddField(
            model_name='event',
            name='link',
            field=models.URLField(default='google.com', max_length=250),
        ),
    ]
