from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            print(fm)
            print('Clear DATA', fm.cleaned_data)
            print('Clear Data', fm.cleaned_data['name'])
            print('Clear Data', fm.cleaned_data['email'])
            print('Clear Data', fm.cleaned_data['password'])
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/registration.html', {'form':fm})

