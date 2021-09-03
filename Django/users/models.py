from django.db import models
from django.contrib.auth.models import User
# Create your models here.
ELIGIBLE_LEAVE=(
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5')
)
GENDER=(
    ('male','Male'),
    ('femae','Female')
)
MANAGER=(
    ('Rakesh','Rakesh'),
    ('Yasin','Yasin'),
    ('Jaya', 'Jaya')
)

class UserProfile(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    password = models.CharField(max_length=10, default='qwerty@123')
    img = models.ImageField(upload_to='profiles', default='default.img', help_text='Upload image with size of 1MB')
    leave_days = models.CharField(max_length=20, choices=ELIGIBLE_LEAVE)
    gender = models.CharField(max_length=20, choices=GENDER)
    manager_name = models.CharField(max_length=50, choices=MANAGER, default='Rakesh')
    bio = models.CharField(max_length=100)