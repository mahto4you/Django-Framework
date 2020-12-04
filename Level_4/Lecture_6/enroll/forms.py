from django import forms
from .models import User

class StudentRegistration(forms.ModelForm):
    class Meta:
        model =User
        #exclude=['name']
        exclude=('name',)
        #fields = '__all__'
       # fields = ['name','password','email']