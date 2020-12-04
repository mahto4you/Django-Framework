from django.shortcuts import render,HttpResponse
from .forms import ContactForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
# Create your views here.

class ContactFormView(FormView):
    template_name = 'school/contact.html'
    form_class = ContactForm
    success_url = '/thankyou/'
    initial = {'name':'Chinu', 'email':'nitish.mahato990@gmail.com'}
    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['msg'])
        return super().form_valid(form)
        # return HttpResponse("Message Bhej Diya Gaya h")

class ThanksTemplateView(TemplateView):
    template_name = 'school/thankyou.html'