from django.urls import path
from . import views
from iti.views import get_iti_courses
from roadmaps.views import get_roadmaps
from session.views import get_sessions
urlpatterns = [
    path('', views.home, name='home'),
    path('aboutus/', views.about, name='aboutus'),
    path('aboutus/iti' , get_iti_courses , name='iti'),
    path('aboutus/roadmaps' , get_roadmaps , name='roadmaps'),
    path('aboutus/sessions' , get_sessions , name='sessions'),
]
