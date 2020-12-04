from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages
# Create your views here.

def regi(request):
    messages.info(request, 'This is info')
    messages.success(request, 'This is Success')
    messages.warning(request, 'This is Warning')
    messages.error(request, 'This is Error')
    fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form':fm})
