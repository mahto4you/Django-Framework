from django.shortcuts import render
from .models import Student, Teacher
# Create your views here.

def home(request):
    #student_data = Student.objects.all()
    #student_data = Student.objects.filter(marks=80)
    #student_data = Student.objects.exclude(marks=80)
    #student_data = Student.objects.order_by('city')
    #student_data = Student.objects.order_by('marks')
    #student_data = Student.objects.order_by('-marks')
    #student_data = Student.objects.order_by('?')
    #student_data = Student.objects.order_by('name')
    #student_data = Student.objects.order_by('-name')
    #student_data = Student.objects.order_by('id')
    #student_data = Student.objects.order_by('id').reverse()
    #student_data = Student.objects.order_by('id').reverse()[:5]
    #student_data = Student.objects.values()
    #student_data = Student.objects.values('name','city')
    #student_data = Student.objects.values_list()
    #student_data = Student.objects.values_list('name', 'city')
    #student_data = Student.objects.values_list('name', 'city', named=True)
    #student_data = Student.objects.using('default')
    #student_data = Student.objects.dates('pass_date', 'year')
    #student_data = Student.objects.dates('pass_date', 'month')
    #student_data = Student.objects.dates('pass_date', 'week')
    #student_data = Student.objects.dates('pass_date', 'day')
    
    ############# Second Table Teacher Started #####################
    
    qs1 = Student.objects.values_list('id', 'name', named=True)
    qs2 = Teacher.objects.values_list('id', 'name', named=True)
    student_data = qs2.union(qs1)
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data)
    return render(request, 'school/home.html', {'students':student_data})