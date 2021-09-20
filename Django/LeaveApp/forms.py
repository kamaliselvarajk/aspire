from django import forms
from django.forms.widgets import DateInput
from .models import LeaveRequest

LEAVE_TYPE=(
    ('Personal leave','Personal Leave'),
    ('Carry forward','Carry Forward'),
    ('Compensatory leave', 'Compensatory Leave')
)

MANAGER=(
    ('Yasin','Yasin'),
    ('Rakesh','Rakesh'),
    ('Jaya', 'Jaya')
)

class DateInput(forms.DateInput):
    input_type = 'date'

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=20)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class LeaveRequestForm(forms.Form):
    emp_name = forms.CharField(disabled=True, required=False)
    leave_reason = forms.CharField(max_length=100, label='Leave Reason', widget=forms.Textarea(attrs={'rows':2, 'cols':23}))
    leave_type = forms.ChoiceField(choices=LEAVE_TYPE, label='Leave Type')
    from_date = forms.DateField(widget=DateInput)
    to_date = forms.DateField(widget=DateInput)
    no_of_days = forms.IntegerField(max_value=3)
    manager_name = forms.CharField(disabled=True, required=False)
 
    def save(self, pk, manager_name):
        emp_app = LeaveRequest.objects.create(leave_reason=self.cleaned_data['leave_reason'], leave_type=self.cleaned_data['leave_type'], from_date=self.cleaned_data['from_date'], to_date=self.cleaned_data['to_date'], no_of_days=self.cleaned_data['no_of_days'], status='requested', emp_name_id=pk, manager_name=manager_name)
        emp_app.save()

class LeaveApproveForm(forms.Form):
    status = forms.ChoiceField(choices=(('Approve','Approve'),('Cancel','Cancel')))
    manager_name = forms.CharField(max_length=20)
    cancel_reason = forms.CharField(max_length=20, required=False)  