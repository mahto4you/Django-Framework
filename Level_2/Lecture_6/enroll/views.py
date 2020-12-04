from django.shortcuts import render
from enroll.models import Student
# Create your views here.
def studentinfo(request):
    stud=Student.objects.all()   # This command used to show all the data in db
    return render(request, 'enroll/studetails.html', {'stu': stud})