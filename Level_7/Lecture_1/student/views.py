from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def setcookie(request):
    response = render(request, 'student/setcookie.html')
    #response.set_cookie('name', 'chinu', max_age=120)
    #response.set_cookie('name', 'chinu', expires=datetime.utcnow()+timedelta(days=2))
    #response.set_cookie('name', 'Nitish', expires=datetime.utcnow()+timedelta(days=2)) #Replace
    response.set_cookie('address', 'Kenduadih Basti', expires=datetime.utcnow()+timedelta(days=2))  # Appends
    return response

def getcookie(request):
    #name = request.COOKIES['name']
    #name = request.COOKIES.get('name')
    name = request.COOKIES.get('name', "Guest")
    return render(request, 'student/getcookie.html', {'name':name})

def delcookie(request):
    response = render(request, 'student/delcookie.html')
    response.delete_cookie('name')
    return response