from django import forms
from django.forms.widgets import RadioSelect
from .models import UserProfile
import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as a
from django.contrib.auth.models import User, Group

GENDER=(
    ('Male','Male'),
    ('Female','Female')
)
MANAGER=(
    ('Rakesh','Rakesh'),
    ('Yasin','Yasin'),
    ('Jaya', 'Jaya')
)

def name_validation(value):
        if not re.findall('[a-zA-Z]', value):
            raise ValidationError(a('Username should contain string only!'))
        else:
            return True

def password_validation(value):        
        if not re.findall('[A-Z]', value):
            raise ValidationError(a('Your password must contain atleast 1 capital letter!'))

        elif not len(value) > 9:
            raise ValidationError(a('Minimum password length is 10!'))

        elif not re.findall('[()[\]|\\`~!@#$%^&*_\-+=;:\'",<>./?]', value):
            raise ValidationError(a('Your  password should contain atleast 1 special character!'))

        else:
            return True
  
class EmployeeCreationForm(forms.Form):
    name = forms.CharField(label='Username',max_length=20 , validators=[name_validation])
    pwd = forms.CharField(label='Password', widget=forms.PasswordInput(), validators=[password_validation])
    img = forms.ImageField(label='Image', required=False)
    leave_days = forms.IntegerField(max_value=3)
    gender = forms.ChoiceField(label='Gender', choices=GENDER)
    manager_name = forms.ChoiceField(label='Manager Name', choices=MANAGER)
    group = forms.ChoiceField(label='Group', choices=(("Employee","Employee"),("Manager","Manager")))
    bio = forms.CharField(label='Bio', max_length=30, widget=forms.Textarea(attrs={'rows':2, 'cols':22}), required=False)

    def save(self):
        user = User.objects.create(username=self.cleaned_data['name'], password=self.cleaned_data['pwd'], is_active='1')
        user_app = UserProfile.objects.create(user_id=user.id, img=self.cleaned_data['img'], leave_days=self.cleaned_data['leave_days'], gender=self.cleaned_data['gender'], manager_name=self.cleaned_data['manager_name'], group=self.cleaned_data['group'], bio=self.cleaned_data['bio'])
        user_app.save()
        groups = Group.objects.get(name=self.cleaned_data['group'])
        groups.user_set.add(user)
        groups.save()
        user.save()    

class ManagerCreationForm(forms.Form):
    name = forms.CharField(label='Username', max_length=20, validators=[name_validation])
    password = forms.CharField(label='Password', widget=forms.PasswordInput(), validators=[password_validation])
    img = forms.ImageField(label='Image', required=False)
    domain = forms.CharField(label='Domain', max_length=20)
    gender = forms.ChoiceField(label='Gender', choices=GENDER)
    group = forms.ChoiceField(label='Group', choices=(("Employee","Employee"),("Manager","Manager")))
    bio = forms.CharField(label='Bio', max_length=30, widget=forms.Textarea(attrs={'rows':2, 'cols':22}), required=False)
     
    def save(self):
        user = User.objects.create(username=self.cleaned_data['name'], password=self.cleaned_data['password'], is_active='1', is_staff='1')
        user_app = UserProfile.objects.create(user_id=user.id, img=self.cleaned_data['img'], domain=self.cleaned_data['domain'], gender=self.cleaned_data['gender'], group=self.cleaned_data['group'], bio=self.cleaned_data['bio'])
        user_app.save()
        groups = Group.objects.get(name=self.cleaned_data['group'])
        groups.user_set.add(user)
        groups.save()
        user.save()       