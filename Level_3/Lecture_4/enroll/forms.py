from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(initial="Nitish", help_text="Hi welcome")
    email = forms.EmailField()