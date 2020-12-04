from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showformdata(request):
    fm = StudentRegistration(initial={'name': 'Dj'})
    return render(request, 'enroll/registration.html', {'form':fm})

