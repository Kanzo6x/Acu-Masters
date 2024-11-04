from django.shortcuts import render
from .models import iti_course
def get_iti_courses(request):
    if request.method == 'GET':
        iti_courses = iti_course.objects.all()
        return render(request , 'iti/iti.html' , {'iti_courses':iti_courses})
