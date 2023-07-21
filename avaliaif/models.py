from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=300)
    image = models.TextField()

class Review(models.Model):
    points = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)

class Comment(models.Model):
    text = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE)
    
