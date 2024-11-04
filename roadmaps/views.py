from django.shortcuts import render
from .models import roadmap
def get_roadmaps(request):
    if request.method == "GET":
        roadmaps = roadmap.objects.all()
        return render(request , 'roadmaps/roadmaps.html' , {'roadmaps':roadmaps})
