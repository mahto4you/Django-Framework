from django.db import models

# Create your models here.
class Student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=70)
    stuemail=models.EmailField(max_length=70)
    stupass=models.CharField(max_length=70)
    # comment=models.CharField(max_length=40, default='not available')
    comment2=models.CharField(max_length=40, default='available')
    comment3=models.CharField(max_length=40)
    # datetime = models.DateTimeField(auto_now_add=True)
    
# default value used when any changes in the models files i.e table
# in the db 
# python manage.py makemigrations
# python manage.py migrate
    