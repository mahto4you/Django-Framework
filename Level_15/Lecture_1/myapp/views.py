from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# Create your views here.

# Function Based View
def myview(request):
    return HttpResponse('<h1>Function Based View </h1>')

# Class Based view

class MyView(View):
    name ='Nitish'
    #name =''
    def get(self, request):
        #return HttpResponse('<h1> Class Based View- GET</h1>')
        return HttpResponse(self.name)
    
class MyViewChild(MyView):
    def get(self, request):
        return HttpResponse(self.name)