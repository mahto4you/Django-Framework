from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def thanks(request):
    return render(request, 'enroll/success.html')
def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print('Form is Validated')
            print('Name', fm.cleaned_data['name'])
            print('Email:', fm.cleaned_data['email'])
            
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/registration.html', {'form':fm})

