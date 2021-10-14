from django import forms
from django.forms.widgets import Textarea
from .models import UserProfile

LEAVE_TYPE=(
    ('personal leave','Personal Leave'),
    ('carry forward','Carry Forward'),
    ('compensatory leave', 'Compensatory Leave')
)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=20)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class LeaveRequestForm(forms.Form):
    emp_name = forms.CharField(disabled=True)
    leave_reason = forms.CharField(max_length=100, label='Leave Reason', widget=forms.Textarea(attrs={'rows':2, 'cols':22}))
    leave_type = forms.ChoiceField(choices=LEAVE_TYPE, label='Leave Type')
    no_of_days = forms.IntegerField(max_value=3)
    manager_name = forms.CharField(label='Manager Name', max_length=30)

class LeaveApproveForm(forms.Form):
    status = forms.ChoiceField(choices=(('Approve','Approve'),('Cancel','Cancel')))
    manager_name = forms.CharField(max_length=20)
    cancel_reason = forms.CharField(max_length=20, required=False)

class UserCreationForm(forms.Form):
    class Meta:
        model = UserProfile
        fields = ['username', 'img', 'leave_days', 'gender']   