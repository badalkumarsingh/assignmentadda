from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Myblog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title