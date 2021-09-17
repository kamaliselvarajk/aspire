from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .models import UserProfile
from .forms import EmployeeCreationForm, ManagerCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='/splogin')
def create_user(request):
    current_user = request.user
    values = UserProfile.objects.all()
    user = User.objects.all()
    return render(request, 'homepage.html', {'current_user':current_user, 'data':values, 'user':user})

@login_required(login_url='/splogin')
def create_employee(request):
    form = EmployeeCreationForm(request.POST)
    manager = UserProfile.objects.filter(group='Manager')
    manager_list = []
    for i in manager:
        user = User.objects.filter(id=i.user_id)
        for j in user: 
            managername = j.username
            manager_list.append(managername)
    if request.method == 'POST':
        if form.is_valid():
            form.save()   
            return redirect('/show')
        else:
            form.save()  
            return redirect('/show')            
    else:
        return render(request, 'employee.html', {'form':form, 'manager_list':manager_list})

@login_required(login_url='/splogin')
def create_manager(request):
    form = ManagerCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()  
            return redirect('/show')
        else:
           form.save() 
           return redirect('/show')            
    else:
        return render(request, 'manager.html', {'form':form})
 
def list_user(request): 
    values = UserProfile.objects.all()
    user = User.objects.all()
    return render(request, "homepage.html", {'data':values, 'user':user}) 