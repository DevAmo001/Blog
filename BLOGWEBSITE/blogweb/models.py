from django.db import models
from datetime import datetime


class Posts(models.Model):
  title = models.CharField(max_length=100)
  content = models.CharField(max_length=100000)
  created_at = models.DateTimeField(default = datetime.now, blank = True)
