from django.shortcuts import render
from django.views import View
from .forms import ContactForm
from django.http import HttpResponse
# Create your views here.

# Function Based

def homefun(request):
    return render(request, 'myapp/home.html')

# Class  Based

class HomeClassView(View):
    def get(self, request):
        return render(request, 'myapp/home.html')

###########################################

def aboutfun(request):
    context = {'msg': 'Welcome to Nitish Function Based View'}
    return render(request, 'myapp/about.html', context)

class AboutClassView(View):
    def get(self, request):
        context = {'msg': 'Welcome to Nitish Class Based View'}
        return render(request, 'myapp/about.html', context)

###########################################

def contactfun(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank YOu Form Submitted!!')
    else:
        form = ContactForm()
    return render(request, 'myapp/contact.html', {'form':form})

class ContactClassView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'myapp/contact.html', {'form':form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse('Thank YOu Form Submitted!!')
            