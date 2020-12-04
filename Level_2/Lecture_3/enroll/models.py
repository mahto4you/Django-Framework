from django.db import models

# Create your models here.

class Student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=70)
    stuemail=models.EmailField(max_length=70)
    stupass=models.CharField(max_length=70)
    def __str__(self):             # This code used to show the particular column name in the database
        return str(self.stuname)

# python manage.py makemigration
# python manage.py migrate
# python manage.py createsuperuser

