from django.shortcuts import render
from .models import Posts

def home(request):
  # posts = Posts.objects.all()
  return render(request, 'index.html')

def blog(request):
  # posts = Posts.objects.all()
  return render(request, 'blog.html')

def post(request, pk):
  posts = Posts.objects.get(id = pk)
  return render(request, 'post.html', {'posts': posts})
