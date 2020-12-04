from django.shortcuts import render,HttpResponse
from customsignal import signals
# Create your views here.
def home(request):
    signals.notification.send(sender=None, request=request, user={'Nitish', 'Mahato'})
    return HttpResponse("This is Home Page")