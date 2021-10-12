from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from demoapp.forms import UserForm
from demoapp.models import Users

# Create your views here.
def create_user(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/showuser')
        else:
            return render(request, 'index.htm', {'form':form})    
       
    return render(request, 'index.htm', {'form':form})

def list_user(request):
    values = list(Users.objects.values())
    return JsonResponse(values, safe = False)
   