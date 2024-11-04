from django.contrib import admin
from .models import Event, EventPhoto

class EventPhotoInline(admin.TabularInline):
    model = Event.photos.through

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name',)
    inlines = [EventPhotoInline]

@admin.register(EventPhoto)
class EventPhotoAdmin(admin.ModelAdmin):
    list_display = ('photo',)
