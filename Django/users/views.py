from django.shortcuts import render, redirect
from django.http.response import HttpResponseRedirect
from .models import UserProfile
from .forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/splogin')
def create_user(request):
    current_user = request.user
    return render(request, 'homepage.html', {'current_user':current_user})

@login_required(login_url='/splogin')
def create_employee(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save() 
            return redirect('/show')
        else:
            print('Invalid form!') 
            messages.info(request, 'Invalid form!') 
            return render(request, 'employee.html', {'form':form})
            return HttpResponseRedirect('/employee')            
    else:
        return render(request, 'employee.html', {'form':form})

@login_required(login_url='/splogin')
def create_manager(request):
    form = UserCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save() 
            return redirect('/show')
        else:
            print('Invalid form!') 
            messages.info(request, 'Invalid form!') 
            return HttpResponseRedirect('/employee')            
    else:
        return render(request, 'manager.html', {'form':form})

def list_user(request): 
    values = UserProfile.objects.all()
    return render(request, "list_of_users.html", {'data':values}) 
