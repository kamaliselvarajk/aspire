from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .models import UserProfile
from .forms import EmployeeCreationForm, ManagerCreationForm, PasswordResetForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url='/splogin')
def create_user(request):
    current_user = request.user
    values = UserProfile.objects.all()
    user = User.objects.all().order_by('-id')
    print(user)
    return render(request, 'homepage.html', {'current_user':current_user, 'data':values, 'user':user})

@login_required(login_url='/splogin')
def create_employee(request):
    form = EmployeeCreationForm(request.POST or None)
    manager = UserProfile.objects.filter(group='Manager')
    manager_list = []
    for i in manager:
        user = User.objects.filter(id=i.user_id)
        for j in user: 
            managername = j.username 
            manager_list.append(managername)
    print( manager_list)       
    if request.method == 'POST':
        print(request.POST['name'])
        print(request.POST['pwd'])
        print(request.POST['img'])
        print(request.POST['leave_days'])
        print(request.POST['gender'])
        print(request.POST['manager_name'])
        print(request.POST['group'])
        print(request.POST['bio'])
        if form.is_valid():
            form.save()   
            return redirect('/show')
        else:
            print('Invalid form') 
            return render(request, 'employee.html', {'form':form, 'manager_list':manager_list})  
    else:
        return render(request, 'employee.html', {'form':form, 'manager_list':manager_list})

@login_required(login_url='/splogin')
def create_manager(request):
    form = ManagerCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
           form.save()  
           return redirect('/show')
        else:
            print('Invalid form') 
            return render(request, 'manager.html', {'form':form})          
    else:
        return render(request, 'manager.html', {'form':form})
 
def list_user(request): 
    values = UserProfile.objects.all()
    user = reversed(User.objects.all())
    print(user)
    return render(request, "homepage.html", {'data':values, 'user':user}) 

def reset_password(request):   
    form = PasswordResetForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():     
           form.save()  
           return redirect('/splogin')
        else:        
           print('Invalid form')   
           return render(request, 'passwordreset.html', {'form':form})     
    else:
        return render(request, 'passwordreset.html', {'form':form})