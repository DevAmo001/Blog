from django.shortcuts import render
from .models import BlogPosts

def home(request):
  # posts = BlogPosts.objects.all()
  return render(request, 'index.html')

def blog(request):
  # posts = BlogPosts.objects.all()
  return render(request, 'blog.html')

def about(request):
  # posts = BlogPosts.objects.all()
  return render(request, 'about.html')

def contact(request):
  # posts = BlogPosts.objects.all()
  return render(request, 'contact.html')

def learn_more(request):
  # posts = BlogPosts.objects.all()
  return render(request, 'learnmore.html')

def post(request, pk):
  posts = BlogPosts.objects.get(id = pk)
  return render(request, 'post.html', {'posts': posts})
