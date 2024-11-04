from django.shortcuts import render
from .models import session

def get_sessions(request):
    if request.method == "GET":
        sessions = session.objects.all()
        return render(request , 'sessions/sessions.html' , {'sessions':sessions})
