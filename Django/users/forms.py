from django import forms
from .models import UserProfile
import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as a

GENDER=(
    ('male','Male'),
    ('femae','Female')
)
MANAGER=(
    ('Rakesh','Rakesh'),
    ('Yasin','Yasin'),
    ('Jaya', 'Jaya')
)

def name_validation(value):
        print('name')
        if not re.findall('[a-zA-Z]', value):
            raise ValidationError(a('Username should contain string only!'))
        else:
            return True

def password_validation(value):
        
        if not re.findall('[A-Z]', value):
            print('password')
            raise ValidationError(a('Your password must contain atleast 1 capital letter!'))

        elif not len(value) > 9:
            raise ValidationError(a('Minimum password length is 10!'))

        elif not re.findall('[()[\]|\\`~!@#$%^&*_\-+=;:\'",<>./?]', value):
            raise ValidationError(a('Your  password should contain atleast 1 special character!'))

        else:
            return True

class UserCreationForm(forms.Form):
    '''class Meta:
        model = UserProfile
        fields = ['username', 'img', 'leave_days', 'gender', 'bio'] 
    emp_name = forms.CharField(disabled=True)'''
    username = forms.CharField(label='Username',max_length=20 , validators=[name_validation])
    password = forms.CharField(label='Password', widget=forms.PasswordInput(),validators=[password_validation])
    img = forms.ImageField(label='Image', required=False)
    leave_days = forms.IntegerField(max_value=3)
    gender = forms.ChoiceField(label='Gender', choices=GENDER)
    manager_name = forms.CharField(label='Manager Name', max_length=30)
    group = forms.ChoiceField(label='Group', choices=(("employee","Employee"),("manager","Manager")))
    bio = forms.CharField(label='Bio', max_length=30, widget=forms.Textarea(attrs={'rows':2, 'cols':22}))

    def save(self):
        username = self.cleaned_data['username']
        password= self.cleaned_data['password']
        img  = self.cleaned_data['img']
        leave_days = self.cleaned_data['leave_days']
        gender  = self.cleaned_data['gender']
        manager_name = self.cleaned_data['manager_name']
        group  = self.cleaned_data['group']
        bio  = self.cleaned_data['bio']
        user_app = UserProfile.objects.create(username=username, password=password, img=img, leave_days=leave_days, gender=gender, manager_name=manager_name, bio=bio)
        user_app.groups.add(group)
        user_app.save()
