from django.db import models
from django.contrib.auth.models import User
from django import forms
# Create your models here.

class Recentpost(models.Model):
    image = models.ImageField(upload_to='recentposts/', null=True, blank=True)
    video = models.FileField(upload_to='recentposts/',null=True, blank=True)
    title = models.CharField(max_length=200)
    message = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.title


class Sermon(models.Model):
    # Fields for the Sermon model
    title = models.CharField(max_length=200)
    preacher = models.CharField(max_length=100)
    date = models.DateField()
    audio = models.FileField(upload_to='sermons/audio/', null=True, blank=True)
    video = models.FileField(upload_to='sermons/video/', null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class Eventchurch(models.Model):
    #field for churchevent model
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/', null=True, blank=True)

    def __str__(self):
        return self.title 
 


class Media(models.Model):
    video = models.FileField(upload_to='uploads/video/',null=True, blank=True) 
    audio = models.FileField(upload_to='uploads/audio/', null=True, blank=True)

   
 