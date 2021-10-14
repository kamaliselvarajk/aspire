from django import forms
from .models import LEAVE_TYPE, LeaveRequest, UserProfile
LEAVE_TYPE=(
    ('personal leave','Personal Leave'),
    ('carry forward','Carry Forward'),
    ('compensatory leave', 'Compensatory Leave')
)

APPROVE=(
    ('approved', 'Approve'),
    ('canceled', 'Cancel')
)
MANAGER=(
    ('yasin', 'Yasin')
)
class UserCreationForm(forms.Form):
    class Meta:
        model = UserProfile
        fields = ['username', 'img', 'leave_days', 'gender']

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=20)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
'''
class LeaveCreationForm(forms.ModelForm):
    class Meta:
        model = LeaveRequest
        fields = ['emp_name', 'leave_reason', 'leave_type', 'manager_name', 'status']
'''
class LeaveRequestForm(forms.Form):
    emp_name = forms.CharField(max_length=30, label='Employee Name', required=False)
    leave_reason = forms.CharField(max_length=100, label='Leave Reason')
    leave_type = forms.ChoiceField(choices=LEAVE_TYPE, label='Leave Type')
    no_of_days = forms.IntegerField(max_value=3)
    manager_name = forms.CharField(label='Manager Name', max_length=30)
    #manager_name = forms.ChoiceField(choices=(('yasin', 'Yasin')), label='Manager Name', disabled=True, required=False)

class LeaveApproveForm(forms.Form):
    #manager_name = forms.CharField(label='Manager Name', max_length=30)
    status = forms.ChoiceField(label='Approve or Cancel', choices=APPROVE)
    #cancel_reason = forms.CharField(label='Cancel Reason', max_length=100)