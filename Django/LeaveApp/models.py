from users.forms import MANAGER
from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

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


class LeaveRequest(models.Model):
    emp_name = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_reason = models.CharField(max_length=100, help_text='What is the reason for your leave?')
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE)
    from_date = models.DateTimeField(default='2021-09-15')
    to_date = models.DateTimeField(default='2021-09-30')
    no_of_days = models.IntegerField(default=1)
    cancel_reason = models.CharField(max_length=100, help_text='What is the reason for cancelling leave?', default='None')
    manager_name = models.CharField(max_length=50, choices=MANAGER)
    status = models.CharField(max_length=100, default='requested')
    

class LeaveApprove(models.Model):
    emp_name = models.ForeignKey(LeaveRequest, on_delete=models.CASCADE, default='')
    status = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=20)
    cancel_reason = models.CharField(max_length=100, default='None')
    #emp_name_id = models.IntegerField()

