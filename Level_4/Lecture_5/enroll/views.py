from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
# Create your views here.

def thanks(request):
    return render(request, 'enroll/success.html')
def showformdata(request):
    if request.method == 'POST':
        pi =User.objects.get(pk=2)    # For Updating
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            #nm = fm.cleaned_data['name']
            #em = fm.cleaned_data['email']
            #pw = fm.cleaned_data['password']
            #reg = User(name=nm,email=em,password=pw) #Insert
            #reg.save()
            #reg = User(id=2,name=nm,email=em,password=pw) #Update
            #reg.save()
            #reg = User(id=2) #Delete
            #reg.delete()
            fm.save()       #For Updating
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/registration.html', {'form':fm})

