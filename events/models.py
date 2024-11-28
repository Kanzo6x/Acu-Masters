from django.db import models

class Event(models.Model):
    name = models.CharField(max_length=255)
    cover_photo = models.ImageField(upload_to='event_covers/')
    photos = models.ManyToManyField('EventPhoto', related_name='event_photos')
    link = models.URLField(max_length= 250 , null= False , blank= False, default="google.com")

    def __str__(self):
        return self.name

class EventPhoto(models.Model):
    photo = models.ImageField(upload_to='event_photos/')
    
    def __str__(self):
        return f"Photo for Event ID {self.id}"
