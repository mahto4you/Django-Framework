from django.shortcuts import render,HttpResponseRedirect
from .forms import SignUpForm, EditUserProfileForm, EditAdminProfileForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.models import User

# Create your views here.

# Signup View Function
def sign_up(request):
    if request.method =='POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully !!')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'enroll/signup.html', {'form':fm})

# loin View Function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully !!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'enroll/userlogin.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/')
            
        
            
            
                
                
    
    

# Profile

def user_profile(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            if request.user.is_superuser == True:
                fm = EditAdminProfileForm(request.POST, instance=request.user)
                users = User.objects.all()
            else:
                fm = EditUserProfileForm(request.POST, instance=request.user)
                users =None
            if fm.is_valid():
                messages.success(request, 'Profile Updated !!!!')
                fm.save()
        else:
            if request.user.is_superuser == True:
               fm = EditAdminProfileForm(instance=request.user)
               users = User.objects.all()
            else:
                fm =EditUserProfileForm(instance=request.user)
                users = None
        return render(request, 'enroll/profile.html', {'name':request.user.username, 'form':fm, 'users':users})
    else:
        return HttpResponseRedirect('/login/')
# Logout

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# Change Password with old Password

def user_change_pass(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Changed Successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'enroll/changepass.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    
# Change Password without old Password

def user_change_pass1(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            fm = SetPasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request, 'Password Changed Successfully')
                return HttpResponseRedirect('/profile/')
        else:
            fm = SetPasswordForm(user=request.user)
        return render(request, 'enroll/changepass1.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
    

def user_detail(request, id):
    if request.user.is_authenticated:
        pi = User.objects.get(pk=id)
        fm =EditAdminProfileForm(instance=pi)
        return render(request, 'enroll/userdetail.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')
            
        