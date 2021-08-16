from django import forms

class LoginForm(forms.Form):
    Email = forms.CharField(label='Email', max_length=50)
    Password = forms.CharField(label='Password', max_length=10)