from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from lms_app.forms import LoginForm
from .forms import *
from .models import *
import pdb
# Create your views here.

@login_required(login_url='/splogin')
def view_approve_details(request): 
    approve = LeaveApprove.objects.filter(status=request.status) #autofill
    return render(request, 'leave_status.html', {'approve':approve})
'''
@login_required(login_url='/splogin')
def view_leave_details(request): 
    approve = LeaveRequest.objects.filter(emp_name=request.user) #autofill
    return render(request, 'leave_details.html', {'approve':approve})
'''
@login_required(login_url='/splogin')
def leave_request(request):
    form = LeaveRequestForm(request.POST)
    user = request.user
    if request.method == 'POST':
        if form.is_valid():
            emp_name = request.user.username
            leave_reason = form.cleaned_data['leave_reason']
            leave_type =form.cleaned_data['leave_type']
            no_of_days = form.cleaned_data['no_of_days']
            manager_name = form.cleaned_data['manager_name']
            user = LeaveRequest.objects.create(leave_reason=leave_reason, leave_type=leave_type, manager_name=manager_name, no_of_days=no_of_days, emp_name_id=request.user.id, status='requested')
            user.save()
            approve = LeaveApprove.objects.create(manager_name=manager_name, status='requested')
            approve.save()
            #return render(request, 'leave_form.html', {'form':form})
        else:
            #print('Invalid form!')
            return HttpResponse('Request sent to manager')
            #return render(request, 'leave_form.html', {'form':form})
    else:
        #print('Something went wrong!')
        #return HttpResponse('/apply')
        return render(request,'leave_form.html',{'form':form})  

def user_profile(request):
    #form = UserCreationForm(request.POST)
    form = UserProfile()
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password') and request.POST.get('img') and request.POST.get('leave_days') and request.POST.get('gender') and request.POST.get('manager_name'):
            
            form.username = request.POST.get('username')
            form.password = request.POST.get('password')
            form.img = request.POST.get('img')
            form.leave_days = request.POST.get('leave_days')
            form.gender = request.POST.get('gender')
            if not form.username.is_staff:
                manager_name = request.POST.get('manager_name')

            form.save()

            #return render(request, 'home_page.html', {form:'form'})
    #return HttpResponse('User created!')
    
    return render(request, 'home_page.html')

@login_required(login_url='/splogin')
def approve_leave(request):
    form = LeaveApproveForm(request.POST)
    user = request.user
    value = LeaveRequest.objects.all()
    if request.method == 'POST':
        if form.is_valid():
            leave_status = form.cleaned_data['status']
            print(value)
            print(leave_status)
            leave_req = LeaveRequest.objects.update(status=leave_status)
            leave_req.save()
            form.save()
            return redirect('/approve')
        else:   
            print('hi')
            #return render(request, 'approve_leave.html', {'fom':form, 'value':value})
    else:
        #return render(request, 'approve_leave.html', {'form':form, 'value':value, 'user':user})
        return HttpResponseRedirect('/approve')
        
   

def user_login(request):
    form = LoginForm(request.POST)

    if request.method=='POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,password=password)

            if user is not None:
                login(request,user)
                if not user.is_superuser and user.is_staff: #Checking manager
                    return HttpResponseRedirect('/approve')
                elif not user.is_staff and user.is_active:  #Checking Employee
                    return HttpResponseRedirect('/apply')
                elif user.is_staff and user.is_superuser:   #checking admin
                    return HttpResponseRedirect('/add')
            else:
                #messages.info("Invalid Login")
                return HttpResponseRedirect('/splogin')
    else:
        
        return render(request,'login_form.html',{'form':form})  

def logout_view(request):
    logout(request)
    #return redirect('splogin/')
    return HttpResponseRedirect('/splogin')