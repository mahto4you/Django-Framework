from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student
# Create your views here.
class StudentListView(ListView):
    model = Student
    # template_name_suffix = '_list'
    template_name_suffix = '_get'
    # ordering = ['name']
    ordering = ['roll']
    
    
    
    
    
    
    # stud = Student.objects.all()
    # context = {'stu':stud}
    # return render(request, 'school/student_list.html', context)
