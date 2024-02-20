from django import forms

class SignUp(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    
class Login(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
    
    