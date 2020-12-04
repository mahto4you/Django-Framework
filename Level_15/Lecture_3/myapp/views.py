from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
# Create your views here.

def newsfun(request, template_name):
    template_name = template_name
    context = {'info':'New Education System Announced'}
    return render(request, template_name, context)


class NewsClassView(View):
    template_name = ''
    def get(self, request):
       context = {'info':'New Education System Announced'}
       return render(request, self.template_name, context)
