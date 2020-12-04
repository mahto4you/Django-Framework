from django.shortcuts import render

# Create your views here.
#def show_details(request, my_id):
    #print(my_id)
#    student = {'id':my_id}
#    return render(request, 'enroll/show.html', student)

def home(request):
    return render(request, 'enroll/home.html')

#def show_details(request, my_id):
#    if my_id==1:
#        student = {'id':my_id, 'name':'Nitish'}
#    if my_id==2:
#        student = {'id':my_id, 'name':'Chinu'}
#    return render(request, 'enroll/show.html', student)

#def show_details(request, my_id):
#    if my_id=='1':
#        student = {'id':my_id, 'name':'Nitish'}
#    if my_id=='2':
#        student = {'id':my_id, 'name':'Chinu'}
#    if my_id=='3':
#        student = {'id':my_id, 'name':'Neha'}    
#    return render(request, 'enroll/show.html', student)

def show_details(request, my_id):
    if my_id==1:
        student = {'id':my_id, 'name':'Nitish'}
    if my_id==2:
        student = {'id':my_id, 'name':'Chinu'}
    if my_id==3:
        student = {'id':my_id, 'name':'Neha'}    
    return render(request, 'enroll/show.html', student)

def show_subdetails(request, my_id, my_subid):
    if my_id==1 and my_subid==5:
        student = {'id':my_id, 'name':'Nitish','info':'subdetails'}
    if my_id==2 and my_subid==6:
        student = {'id':my_id, 'name':'Chinu','info':'subdetails'}
    if my_id==3 and my_subid==7:
        student = {'id':my_id, 'name':'Neha','info':'subdetails'}    
    return render(request, 'enroll/show.html', student)