from django.shortcuts import render
#from django.http import HttpResponseRedirect
from .forms import StudentRegistration
# Create your views here.

def thanks(request):
    return render(request, 'enroll/success.html')
def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            print('Clear Data', fm.cleaned_data['name'])
            print('Clear Data', fm.cleaned_data['email'])
            print('Clear Data', fm.cleaned_data['password'])
            #return HttpResponseRedirect('/reg/success/')
            return render(request, 'enroll/success.html', {'nm':name})
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/registration.html', {'form':fm})

