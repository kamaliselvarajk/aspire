from django.db import models
#from django import forms

# Create your models here.

LEAVE_CHOICE=[
    ('personal leave','Personal Leave'),
    ('carry forward','Carry Forward'),
    ('compensatory leave', 'Compensatory Leave')
]

class EmployeeAction(models.Model):
    empname = models.CharField(max_length=50, default="Individual")
    leave_reason = models.CharField(max_length=100, default="Individual")
    request = models.CharField(max_length=50, default="Individual")
    leave_type = models.CharField(max_length=20, choices=LEAVE_CHOICE, default="Individual")
