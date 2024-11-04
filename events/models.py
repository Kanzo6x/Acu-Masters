from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    cover_photo = models.ImageField(upload_to='event_covers/')
    photos = models.ManyToManyField('EventPhoto', related_name='event_photos')
    video = models.FileField(upload_to='event_videos/', blank=True, null=True)

    def __str__(self):
        return self.name

class EventPhoto(models.Model):
    photo = models.ImageField(upload_to='event_photos/')
    
    def __str__(self):
        return f"Photo for Event ID {self.id}"
