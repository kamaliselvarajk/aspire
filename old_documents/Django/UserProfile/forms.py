from django import forms
from django.forms.widgets import Textarea
import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as a

def password_validation(value):
        if not len(re.findall('\d', value)) >= 3:
            raise ValidationError(a('Your password must contain atleast 3 numbers!'))

        elif not len(value) > 10:
            raise ValidationError(a('Minimum password length is 11!'))

        elif not re.findall('[()[\]|\\`~!@#$%^&*_\-+=;:\'",<>./?]', value):
            raise ValidationError(a('Your  password should contain atleast 1 special character!'))

        else:
            return True

class RegistrationForm(forms.Form):
    
    username = forms.CharField(label='User Name', max_length=100)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password',widget=forms.PasswordInput(),validators=[password_validation])
    gender = forms.ChoiceField(label='Gender',choices=(('male','Male'),('female','Female')))
    #admincheck = forms.ChoiceField(label="Admin User",widget=forms.CheckboxInput())
    dob = forms.DateField(label='Date of Birth')
    bio = forms.CharField(label='Bio',required=False)


#save function-create, handle
class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=20)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())