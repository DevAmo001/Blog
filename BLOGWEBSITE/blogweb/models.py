from django.db import models
from datetime import datetime


class BlogPosts(models.Model):
  title = models.CharField(max_length=100)
  content = models.CharField(max_length=100000)
  date = models.DateTimeField(default = datetime.now, blank = True)
  likes = models.IntegerField(default = 0)
  comments = models.IntegerField(default = 0)
  author = models.CharField(max_length=100)
  image = models.ImageField(upload_to='static/assets/img', default='static/assets/img/Code-AI.png')
