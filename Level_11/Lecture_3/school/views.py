from django.shortcuts import render
from .models import Student
from datetime import date, time
# Create your views here.

def home(request):
    #student_data = Student.objects.all()
    #student_data = Student.objects.filter(name__exact='Nitish')
    #student_data = Student.objects.filter(name__iexact='nitish')
    #student_data = Student.objects.filter(name__contains='i')
    #student_data = Student.objects.filter(name__icontains='I')
    #student_data = Student.objects.filter(id__in=[1,2,7])
    #student_data = Student.objects.filter(marks__in=[60,70])
    #student_data = Student.objects.filter(marks__gt=60)
    #student_data = Student.objects.filter(marks__gte=60)
    #student_data = Student.objects.filter(marks__lt=80)
    #student_data = Student.objects.filter(marks__lte=60)
    #student_data = Student.objects.filter(name__startswith='S')
    #student_data = Student.objects.filter(name__istartswith='s')
    #student_data = Student.objects.filter(name__endswith='t')
    #student_data = Student.objects.filter(name__iendswith='T')
    #student_data = Student.objects.filter(passdate__range=('2020-03-04', '2020-06-05'))
    #student_data = Student.objects.filter(admdatetime__date=date(2020,3,4))
    #student_data = Student.objects.filter(admdatetime__date__gt=date(2020,3,4))
    #student_data = Student.objects.filter(passdate__year=2020)
    #student_data = Student.objects.filter(passdate__month=4)
    #student_data = Student.objects.filter(passdate__month__gt=4)
    #student_data = Student.objects.filter(passdate__month__gte=4)
    #student_data = Student.objects.filter(passdate__day=2)
    #student_data = Student.objects.filter(passdate__day__gt=2)
    #student_data = Student.objects.filter(passdate__week=14)
    #student_data = Student.objects.filter(passdate__week_day=5)
    #student_data = Student.objects.filter(passdate__week_day__gt=5)
    #student_data = Student.objects.filter(passdate__quarter=1)
    #student_data = Student.objects.filter(passdate__quarter=2)
    #student_data = Student.objects.filter(admdatetime__time__gt=time(6,00))
    #student_data = Student.objects.filter(admdatetime__hour__gt=5)
    #student_data = Student.objects.filter(admdatetime__minute__gt=12)
    #student_data = Student.objects.filter(admdatetime__second__gt=10)
    #student_data = Student.objects.filter(roll__isnull=True)
    student_data = Student.objects.filter(roll__isnull=False)
    print("Return: ", student_data)
    print()
    print("SQL Query: ", student_data.query)
    return render(request, 'school/home.html', {'students':student_data})
