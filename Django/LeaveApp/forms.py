from django import forms
from django.forms.widgets import DateInput, Textarea
from .models import LeaveRequest


LEAVE_TYPE=(
    ('personal leave','Personal Leave'),
    ('carry forward','Carry Forward'),
    ('compensatory leave', 'Compensatory Leave')
)
MANAGER=(
    ('Yasin','Yasin'),
    ('Rakesh','Rakesh'),
    ('Jaya', 'Jaya')
)

class LoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=20)
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

class LeaveRequestForm(forms.Form):
    emp_name = forms.CharField(disabled=True)
    leave_reason = forms.CharField(max_length=100, label='Leave Reason', widget=forms.Textarea(attrs={'rows':2, 'cols':22}))
    leave_type = forms.ChoiceField(choices=LEAVE_TYPE, label='Leave Type')
    from_date = forms.DateField(widget=DateInput)
    to_date = forms.DateField(widget=DateInput)
    no_of_days = forms.IntegerField(max_value=3)
    manager_name = forms.ChoiceField(label='Manager Name', choices=MANAGER)

    def save(self, pk):
        leave_reason = self.cleaned_data['leave_reason']
        leave_type= self.cleaned_data['leave_type']
        no_of_days  = self.cleaned_data['no_of_days']
        from_date = self.cleaned_data['from_date']
        to_date = self.cleaned_data['to_date']
        manager_name = self.cleaned_data['manager_name']
        emp_app = LeaveRequest.objects.create(leave_reason=leave_reason, leave_type=leave_type, from_date=from_date, to_date=to_date, no_of_days=no_of_days, manager_name=manager_name, status='requested', emp_name_id=pk)
        emp_app.save()

class LeaveApproveForm(forms.Form):
    status = forms.ChoiceField(choices=(('Approve','Approve'),('Cancel','Cancel')))
    manager_name = forms.CharField(max_length=20)
    cancel_reason = forms.CharField(max_length=20, required=False)

  