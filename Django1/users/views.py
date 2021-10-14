from django.shortcuts import render, redirect
from .models import UserProfile
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from LeaveApp.forms import UpdateManagerForm

# Create your views here.

@login_required(login_url='/splogin')
def list_user(request):
    current_user = request.user
    values = UserProfile.objects.all()
    user = User.objects.all()
    return render(request, 'users/homepage.html', {'current_user':current_user, 'data':values, 'user':user})

@login_required(login_url='/splogin')
def create_employee(request):
    form = EmployeeCreationForm(request.POST or None)    
    if request.method == 'POST':
        if form.is_valid():
            form.save()   
            return redirect('/add')
        else:
            return render(request, 'users/employee.html', {'form':form})  
    else:
        return render(request, 'users/employee.html', {'form':form})

@login_required(login_url='/splogin')
def create_manager(request):
    form = ManagerCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
           form.save()  
           return redirect('/add')
        else: 
            return render(request, 'users/manager.html', {'form':form})          
    else:
        return render(request, 'users/manager.html', {'form':form})
 
def reset_password(request):   
    form = PasswordResetForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():     
           form.save()  
           return redirect('/splogin')
        else:          
           return render(request, 'users/passwordreset.html', {'form':form})     
    else:
        return render(request, 'users/passwordreset.html', {'form':form})

def update_man(request, pk): 
    header = 'Update Profile'
    form = UpdateManagerForm(request.POST or None)
    user = User.objects.get(id=pk)
    value = UserProfile.objects.get(user_id=pk)
    if request.method == 'POST':
        if form.is_valid():
            form.save(pk)
            return redirect('/add')
        else:
            return render(request, 'users/manager_update.html', {'form':form, 'user':user, 'value':value, 'header':header})    
    else:
        return render(request, 'users/manager_update.html', {'form':form, 'user':user, 'value':value, 'header':header}) 
                            