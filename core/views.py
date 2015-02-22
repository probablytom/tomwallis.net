from django.shortcuts import render
from core.models import Post

def home(request):
    return render(request, 'home.html', {'posts': Post.objects.all()})


