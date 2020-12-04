from django import forms
class StudentRegistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput)
    password = forms.CharField(widget=forms.PasswordInput)
    def clean(self):
        clean_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']
        if len(valname)<4:
            raise forms.ValidationError('Name Should be more than or equal 4')
        
        if len(valemail)<10:
            raise forms.ValidationError('Email Should be more than or equal 4')
        
        