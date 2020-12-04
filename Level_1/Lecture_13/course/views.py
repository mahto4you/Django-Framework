from django.shortcuts import render

# Create your views here.
def learn_django(request):
    return render(request, 'course/info.htm', {'nm':'Django Course'})

def home(request):
    return render(request, 'Home.htm', {'nm':'Django Home'})