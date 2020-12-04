from django.shortcuts import render
from django.core.cache import cache
# Create your views here.

#def home(request):
    #mv = cache.get_or_set('fees', 5000, 30)
    #mv = cache.get_or_set('Movie', 'Don', 30)
    #mv = cache.get_or_set('fees', 2000, 30, version=2)
    #return render(request, 'enroll/course.html', {'fm':mv})

#def home(request):
#    data = {'name':'Nitish', 'roll':102}
#    cache.set_many(data, 30)
#    sv = cache.get_many(data)
#    print(sv)
#    return render(request, 'enroll/course.html', {'stu':sv})

#def home(request):
    #cache.delete('roll')
#    cache.delete('fees', version=2)
#    return render(request, 'enroll/course.html')

#def home(request):
    #dv = cache.decr('roll', delta=2)
    #dv = cache.incr('roll', delta=2)
    #print(dv)
    #return render(request, 'enroll/course.html')

def home(request):
    cache.clear()
    return render(request, 'enroll/course.html')