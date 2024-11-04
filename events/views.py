from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Event

class EventListView(ListView):
    model = Event
    template_name = 'events/events.html'  # Using 'events.html' as the template name
    context_object_name = 'events'

class EventDetailView(DetailView):
    model = Event
    template_name = 'events/event_detail.html'
    context_object_name = 'event'
