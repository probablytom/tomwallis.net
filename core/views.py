from django.shortcuts import render
from core.models import Post, Project

def home(request):
    return render(request, 'home.html', {'posts': Post.objects.all()})

def projects(request):
    return render(request, 'projects.html', {'projects': Project.objects.all()})