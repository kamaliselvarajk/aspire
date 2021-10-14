from LeaveApp.models import LeaveApprove, LeaveRequest
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect, HttpResponse
from django.db.models import Q

# Create your views here.
@login_required(login_url='/splogin')
def request_leave(request):
    form = LeaveRequestForm(request.POST, initial={'emp_name':request.user})
    current_user = request.user
    if request.method=='POST':
        if form.is_valid():
            leave_reason = form.cleaned_data['leave_reason']
            leave_type =form.cleaned_data['leave_type']
            no_of_days = form.cleaned_data['no_of_days']
            manager_name = form.cleaned_data['manager_name']

            empapp = LeaveRequest(leave_reason=leave_reason, leave_type=leave_type, no_of_days=no_of_days, manager_name=manager_name, status='requested', emp_name_id=request.user.id)
            empapp.save()
            #manapp = LeaveApprove(manager_name=manager_name, status='requested', emp_name_id=request.user.id)
            #manapp.save()
            return redirect('/leavedetails')
        else:
            #return render(request, 'leave_form.html', {'form':form})
            print('Invalid form!')
    else:
        return render(request, 'leave_form.html', {'form':form, 'current_user':current_user})


@login_required(login_url='/splogin')
def approve_leave(request):
    form = LeaveApproveForm(request.POST)
    current_user = request.user
    #print(request.POST.id)
    value = LeaveRequest.objects.filter(status='requested')
    if request.method == 'POST':
        print('Yasin')
        #print(request.POST['status'])
        if form.is_valid():
            
            statuss = request.POST.get('status')
            empapp = LeaveRequest()
            empapp.status = statuss
            print(empapp.status)
            empapp.save()
            return redirect('/approve')
        else:
            #return HttpResponse('Invalid form')
            return render(request, 'approve_form.html', {'form':form, 'value':value, 'current_user':current_user})
            #print('Invalid form')
    else:
        return render(request, 'approve_form.html', {'form':form, 'value':value, 'current_user':current_user})


@login_required(login_url='/splogin')
def leave_details(request):
    current_user = request.user
    approve = LeaveRequest.objects.filter(emp_name=request.user) #autofill
    return render(request, 'leave_details.html', {'approve':approve, 'current_user':current_user})


@login_required(login_url='/splogin')
def leave_status(request):
    current_user = request.user
    approve = LeaveRequest.objects.filter((Q(status='approved') | Q(status='cancelled')), emp_name=request.user) #autofill
    return render(request, 'leave_details.html', {'approve':approve, 'current_user':current_user})

@login_required(login_url='/splogin')
def approve(request,pk):
    empapp = LeaveRequest.objects.get(emp_name_id=pk, status='requested')
    empapp.status = 'approved'
    empapp.save()
    return redirect('/approve')
    #manapp = LeaveApprove.objects.get(emp_name_id=pk)[:1]
    #manapp.status = 'approved'
    #manapp.save() emp_name_id=pk

@login_required(login_url='/splogin')
def cancel(request,pk):
    cancel_reason = 'You have an important work'
    #form = LeaveApproveForm(request.POST)
    #if request.method=='POST':
    #    if form.is_valid():
    #       cancel_reason = form.cleaned_data['cancel_reason']

           #app = LeaveApprove(cancel_reason=cancel_reason)
           #app.save()
    empapp = LeaveRequest.objects.get(emp_name_id=pk, status='requested')
    empapp.status = 'cancelled'
    empapp.save()
    return redirect('/approve')
    #manapp = LeaveApprove.objects.get(emp_name_id=pk)[:1]
    #manapp.status = 'cancelled'
    #manapp.save()

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
                elif user.is_staff and user.is_superuser:   #Checking admin
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
    
    return render(request, 'homepage.html')