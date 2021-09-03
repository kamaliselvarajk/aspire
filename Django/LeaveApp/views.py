from LeaveApp.models import LeaveApprove, LeaveRequest
from django.shortcuts import redirect, render
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect, HttpResponse
from django.db.models import Q
from django.contrib import messages

# Create your views here.
@login_required(login_url='/splogin')
def request_leave(request):
    header = 'Apply Leave'
    form = LeaveRequestForm(request.POST, initial={'emp_name':request.user})
    current_user = request.user
    id = request.user.id
    if request.method=='POST':
        if form.is_valid():
            form.save(id)
            return redirect('/leavedetails')
        else:
            print('Invalid form!')
    else:
        return render(request, 'leaveapp/leave_form.html', {'form':form, 'current_user':current_user, 'header':header})


@login_required(login_url='/splogin')
def approve_leave(request):
    header = 'Approve\Cancel Leave'
    form = LeaveApproveForm(request.POST)
    current_user = request.user
    value = LeaveRequest.objects.filter(status='requested')
    if request.method == 'POST':
        if form.is_valid():
            '''statuss = request.POST.get('status')
            emp_app = LeaveRequest()
            emp_app.status = statuss
            print(emp_app.status)
            emp_app.save()'''
            return redirect('/approve')
        else:
            #return HttpResponse('Invalid form')
            return render(request, 'leaveapp/approve_form.html', {'form':form, 'value':value, 'current_user':current_user})
            #print('Invalid form')
    else:
        return render(request, 'leaveapp/approve_form.html', {'form':form, 'value':value, 'current_user':current_user, 'header':header})


@login_required(login_url='/splogin')
def leave_details(request):
    header = 'Requested Leave'
    current_user = request.user
    approve = LeaveRequest.objects.filter(emp_name=request.user, status='requested') #autofill
    return render(request, 'leaveapp/leave_details.html', {'approve':approve, 'current_user':current_user, 'header':header})


@login_required(login_url='/splogin')
def leave_status(request):
    header = 'Leave History'   
    current_user = request.user
    approve = LeaveRequest.objects.filter((Q(status='approved') | Q(status='cancelled')), emp_name=request.user) #autofill
    return render(request, 'leaveapp/leave_details.html', {'approve':approve, 'current_user':current_user, 'header':header})

@login_required(login_url='/splogin')
def approve(request,pk):
    emp_app = LeaveRequest.objects.get(emp_name_id=pk, status='requested')
    emp_app.status = 'approved'
    emp_app.save()
    return redirect('/approve')

@login_required(login_url='/splogin')
def cancel(request,pk,slug):
    emp_app = LeaveRequest.objects.get(emp_name_id=pk, status='requested')
    emp_app.status = 'cancelled'
    print(slug)
    emp_app.cancel_reason = slug
    emp_app.save()
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
                messages.info(request, "Invalid Login")
                return redirect('/splogin')
                          
    else:
        return render(request,'leaveapp/login_form.html',{'form':form})
    # return HttpResponseRedirect('/splogin')

def logout_view(request):
    logout(request)
    #return redirect('splogin/')
    return HttpResponseRedirect('/splogin')

