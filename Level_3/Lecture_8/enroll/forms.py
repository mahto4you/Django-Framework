from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(widget=forms.PasswordInput())
    address = forms.CharField(widget=forms.HiddenInput())
    address1 = forms.CharField(widget=forms.CheckboxInput())
    address2 = forms.CharField(widget=forms.FileInput())
    name1 = forms.CharField(widget=forms.TextInput(attrs={'class':'somecss1'}))