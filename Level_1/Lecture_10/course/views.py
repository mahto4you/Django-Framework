from django.shortcuts import render

# Create your views here.

#def learn_django(request):
 #   coursename={'cname': 'Django'}
  #  return render(request, 'course/courseone.htm',
   # context=coursename)

def learn_django(request):
    return render(request, 'course/courseone.htm', {'cname': 'Django'})