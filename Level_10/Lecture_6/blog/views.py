from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    print("I am view")
    return HttpResponse("This is Home Page")

def excp(request):
    print("I am Excp View")
    a = 10/0
    return HttpResponse("This is Excp Page")