from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showformdata(request):
    fm = StudentRegistration()
    fm.order_fields(field_order=['email', 'first_name', 'name'])
    #fm.order_fields(field_order=['name', 'first_name', 'email'])
    return render(request, 'enroll/registration.html', {'form':fm})

