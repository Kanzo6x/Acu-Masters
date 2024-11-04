from django.urls import path
from .views import show_cards
urlpatterns = [
    path('' , show_cards , name='contact_us'),
]
