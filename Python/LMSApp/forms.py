from django import forms
from LMSApp.models import EmployeeAction

'''
LEAVE_CHOICE=[
    ('personal leave','Personal Leave'),
    ('carry forward','Carry Forward'),
    ('compensatory leave', 'Compensatory Leave')
]
class EmployeeAction(forms.Form):
    empname = forms.CharField(max_length=30, label='Employee Name', widget=forms.TextInput(attrs={'autocomplete':'off'}))
    leave_reason = forms.CharField(max_length=100, label='Leave Reason')
    request = forms.CharField(max_length=50, label='Requesting to', widget=forms.TextInput(attrs={'autocomplete':'off'}))
    leave_type = forms.ChoiceField(label='Leave Type', choices=LEAVE_CHOICE)
    #leave_type = forms.ChoiceField(label='Leave Type',choices=(('personal leave','Personal Leave'),('carry forward','Carry Forward'),('compensatory leave', 'Compensatory Leave')))
''' 
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = EmployeeAction
        fields = ['empname', 'leave_reason', 'request', 'leave_type']



