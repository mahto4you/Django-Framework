from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=80)
    roll = models.IntegerField()
    
    #objects = models.Manager()
    student = models.Manager()