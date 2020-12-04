from django.shortcuts import render
from .models import Student, Teacher
# Create your views here.

def home(request):
    #student_data = Student.objects.get(pk=1)
    #student_data = Student.objects.get(id=1)
    #student_data = Student.objects.get(name='Chinu')
    #student_data = Student.objects.first()
    #student_data = Student.objects.order_by('name').first()
    #student_data = Student.objects.last()
    #student_data = Student.objects.latest('pass_date')
    #student_data = Student.objects.earliest('pass_date')
    
    #student_data = Student.objects.all()
    #print(student_data.exists())
    #one_data = Student.objects.get(pk=1)
    #print(student_data.filter(pk=one_data.pk).exists())
    
    #student_data = Student.objects.create(name='Sangam', roll=114, city='Noida', marks=60, pass_date='2020-5-4')
    
    #student_data, created = Student.objects.get_or_create(name='Bhaga', roll=115, city='Bokaro', marks=60, pass_date='2020-8-4')
    
    #student_data = Student.objects.filter(id=9).update(name='Bajrangi', marks=70)
    
    #student_data = Student.objects.filter(marks=60).update(city='Kenduadih')
    
    #student_data, created= Student.objects.update_or_create(id=11, name='Bhaga', defaults={'name':'Shivam'})
    #print(created)
    
    #objs =[
    #    Student(name='Atif', roll=116, city='Dhanbad', marks=70, pass_date='2020-5-4'),
    #    Student(name='Sushil', roll=117, city='Bokaro', marks=80, pass_date='2020-5-6'),
    #    Student(name='Kaif', roll=118, city='Dhanbad', marks=60, pass_date='2020-5-9'),
    #]
    #student_data = Student.objects.bulk_create(objs)
    
    #all_student_data = Student.objects.all()
    #for stu in all_student_data:
    #    stu.city ='Bhai'
    #student_data = Student.objects.bulk_update(all_student_data, ['city'])
    
    #student_data = Student.objects.in_bulk([1,2])
    #student_data = Student.objects.in_bulk([])
    #student_data = Student.objects.in_bulk()
    #print(student_data[1])
    #print(student_data[1].name)
    #print(student_data[2].name)
    
    #student_data = Student.objects.get(pk=13).delete()
    #student_data = Student.objects.filter(marks=70).delete()
    #student_data = Student.objects.all().delete()
    
    
    student_data = Student.objects.all()
    print(student_data.count())
    
    
    print("Return: ", student_data)
    return render(request, 'school/home.html', {'student':student_data})