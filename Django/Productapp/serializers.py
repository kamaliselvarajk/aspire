from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Productapp.models import Product


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'cost', 'currency', 'category', 'colour']

