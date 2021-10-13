from django import forms
from django.forms.widgets import PasswordInput

class RegisterForm(forms.Form):
    name = forms.CharField(label='name', max_length=100)
    username = forms.CharField(label='username', max_length=100)
    email = forms.CharField(label='email', max_length=100)
    password = forms.CharField(label='password', max_length=100, widget=PasswordInput)
    confirm = forms.CharField(label='confirm password', max_length=100, widget=PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password', max_length=100, widget=PasswordInput)



    