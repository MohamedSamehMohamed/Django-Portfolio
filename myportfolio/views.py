from django.shortcuts import render
from .models import Project

def home(request):
    Projects = Project.objects.all()
    return render(request, 'myportfolio/home.html', {'projects': Projects})
