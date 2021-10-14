from django.shortcuts import render
from .models import EmployeeAction


def add_emp_leave(request):
    #form = EmployeeAction(request.POST or None)
    if request.method=='POST':
        if request.POST.get('empname') and request.POST.get('leave_reason') and request.POST.get('request') and request.POST.get('leave_type'):
            form = EmployeeAction()
            #if form.is_valid():
            '''empname = form.cleaned_data['empname']
            leave_reason = form.cleaned_data['leave_reason']
            request = form.cleaned_data['request']
            leave_type = form.cleaned_data['leave_type']'''
            form.empname = request.POST.get('empname')
            form.leave_reason = request.POST.get('leave_reason')
            form.request = request.POST.get('request')
            form.leave_type = request.POST.get('leave_type')
            form.save()
    return render(request, 'home.html')
    #return render(request, 'home.html', {'form':form})
'''
def leave_type(request):
    pl = EmployeeAction.objects.filter(leave_type='Personal Leave')
    cl = EmployeeAction.objects.filter(leave_type='Compensatory Leave')
    cf = EmployeeAction.objects.filter(leave_type='Carry Forward')
    return render(request, "leave_filter.html", {'peronal':pl}, {'compensatory':cl}, {'carry':cf})
'''
def pl(request):
    pl = EmployeeAction.objects.filter(leave_type='Personal Leave')
    return render(request, "leave_filter.html", {'data':pl})

def cl(request):
    cl = EmployeeAction.objects.filter(leave_type='Compensatory Leave')
    return render(request, "leave_filter.html", {'data':cl})

def cf(request):
    cf = EmployeeAction.objects.filter(leave_type='Carry Forward')
    return render(request, "leave_filter.html", {'data':cf})

