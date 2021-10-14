from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    cost = models.IntegerField()
    currency = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    colour = models.CharField(max_length=20)
