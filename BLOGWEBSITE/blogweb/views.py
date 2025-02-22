from django.shortcuts import render
from .models import Posts

def home(request):
  posts = Posts.objects.all()
  return render(request, 'index.html', {'posts': posts})
