from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse
# Create your views here.
def home(request):
    print("I am view")
    return HttpResponse("This is Home Page")

def user_info(request):
    print("I am User Info View")
    context = {'name':'Chinu'}
    return TemplateResponse(request, 'blog/user.html', context)