from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Subject(models.Model):
    text = models.CharField(max_length=200)
    desc = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.text        
class Topic(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    #userrs
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #------
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'topics'
    def __str__(self):
        return self.text
    
class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    #userrs
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    #images
    img = models.ImageField(upload_to='pics', default="pics/default.jpg")
    #------
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
            return self.text
        
    
     