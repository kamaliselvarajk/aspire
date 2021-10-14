from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.deletion import CASCADE

# Create your models here.
LEAVE_TYPE=[
    ('personal leave','Personal Leave'),
    ('carry forward','Carry Forward'),
    ('compensatory leave', 'Compensatory Leave')
]
ELIGIBLE_LEAVE=[
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5')
]
GENDER=[
    ('male','Male'),
    ('femae','Female')
]
MANAGER=[
    ('james', 'James'),
    ('jhon', 'Jhon'),
    ('sofi', 'Sofi'),
    ('jaya', 'Jaya'),
    ('antony', 'Antony')
]

class UserProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profiles', default='default.img', help_text='Upload image with size of 1MB')
    leave_days = models.CharField(max_length=20, choices=ELIGIBLE_LEAVE)
    gender = models.CharField(max_length=20, choices=GENDER)
    
    '''is_employee = models.BooleanField('Is Employee')

    if is_employee==True:
        manager_name = models.CharField(max_length=20, choices=MANAGER)
        designation = models.CharField(max_length=20, default='Employee')
    else:
        designation = models.CharField(max_length=20, default='Manager')
    '''


class LeaveRequest(models.Model):
    emp_name = models.ForeignKey(User, on_delete=models.CASCADE)
    leave_reason = models.CharField(max_length=100, help_text='What is the reason for your leave?')
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPE)
    no_of_days = models.IntegerField(default=1)
    cancel_leave = models.CharField(max_length=100, help_text='What is the reason for cancelling leave?', default='None')
    manager_name = models.CharField(max_length=50)
    status = models.CharField(max_length=20, default='requested')

class LeaveApprove(models.Model):
    manager_name = models.CharField(max_length=20, default='1')
    #manager_name = models.ForeignKey(User, on_delete=CASCADE)
    status = models.CharField(max_length=20)
    #cancel_reason = models.CharField(max_length=100)
