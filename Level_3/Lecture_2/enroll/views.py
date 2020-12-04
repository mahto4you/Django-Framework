from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showformdata(request):
    # fm = StudentRegistration(auto_id=True, label_suffix=' ', initial={'name' : 'Nitish', 'email' : 'nitish.mahato990@gmail.com'})
    # fm = StudentRegistration(auto_id=True, label_suffix=' ', initial={'name' : 'Nitish'})
    # fm = StudentRegistration(auto_id=False, label_suffix=' ', initial={'name' : 'Nitish'})
    # fm = StudentRegistration(auto_id=True, label_suffix=' = ')
    #fm = StudentRegistration(auto_id=True, label_suffix=' ')
    fm = StudentRegistration(auto_id=False)
    #fm = StudentRegistration(auto_id=True)
    # fm = StudentRegistration(auto_id='some_%s')
    return render(request, 'enroll/registration.html', {'form':fm})

