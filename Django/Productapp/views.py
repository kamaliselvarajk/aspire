from django.shortcuts import render, redirect
from Productapp.models import Product
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth
#from django.contrib.messages import constants as messages
#from django.contrib.auth.decorators import login_required
from rest_framework import viewsets, permissions
from Productapp.serializers import UserSerializer

# Create your views here.
@login_required(login_url='login/')
def add_product(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('cost') and request.POST.get('currency') and request.POST.get('category') and request.POST.get('colour'):
            form = Product()
            form.name = request.POST.get('name')
            form.cost = request.POST.get('cost')
            form.currency = request.POST.get('currency')
            form.category = request.POST.get('category')
            form.colour = request.POST.get('colour')
            form.save()
    return render(request, 'index.html')

@login_required(login_url='login/')
def display(request):
    values=Product.objects.all()
    return render(request, "output.html", {'data':values})



def form(request):
    return render(request, 'forms.html')

def logout(request):
    auth.logout(request)
    return redirect('login/')

class UserViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

