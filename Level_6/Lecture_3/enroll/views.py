from django.shortcuts import render
from .forms import StudentRegistration
from django.contrib import messages
# Create your views here.

def regi(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request, 'Your Account has been created !!!')
            print(messages.get_level(request))
            messages.info(request, 'Now You can Login !!!')
            print(messages.get_level(request))
            messages.debug(request, 'This is Debug')
            messages.set_level(request, messages.DEBUG)
            messages.debug(request, 'This is New Debug')
            print(messages.get_level(request))
            
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/userregistration.html', {'form':fm})
