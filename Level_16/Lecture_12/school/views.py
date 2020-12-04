from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Student
from django.views.generic.base import TemplateView
from .forms import StudentForm
# Create your views here.

class StudentCreateView(CreateView):
   form_class = StudentForm
   template_name = 'school/student_form.html'
   success_url = '/thanks/'
    
class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'
    