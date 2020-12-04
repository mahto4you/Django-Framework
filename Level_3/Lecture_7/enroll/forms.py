from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField(label='Your Name', label_suffix=' ', 
                           initial='Nitish', required=False, disabled=True,
                           help_text='limit 30 char')
    