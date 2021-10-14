from django import forms
from UserProfile.models import UserInfo
from django.core.checks import messages
from django.contrib import messages,auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, Group
from Productapp.views import *
from .models import UserInfo
from .forms import RegistrationForm,LoginForm



def register(request):
    title = "Register Here"
    users = RegistrationForm(request.POST)
    if request.method == 'POST':
        if users.is_valid():
            print("valid")
            username = users.cleaned_data['username']
            email = users.cleaned_data['email'] 
            password = users.cleaned_data['password'] 
            gender = users.cleaned_data['gender']
            dob = users.cleaned_data['dob']
            bio = users.cleaned_data['bio']
            #isAdmin = users.cleaned_data['admincheck']
            #print(isAdmin)

            if(password):
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                user_new = UserInfo.objects.create(gender=gender,dob=dob,bio=bio,user_id=user.id)
                user_new.save()
                messages.info(request,"User Created!")
                #print("Use")
                return redirect('login/')

            else:
                messages.info(request,"Invalid user!")

        else:
            return redirect('login/')
            #messages.info(request,"Invalid inputs")

    return render(request,"register.html",{'form':users,'title':title}) 


def login(request):
    title = "Login"
    form = LoginForm(request.POST)

    if request.method=='POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request,user)
                print('Login')
                #if request.user.is_authenticated:
                return redirect('show/')

            else:
                #messages.info("Invalid Login")
                return redirect('show/')
    else:

        return render(request,'loginform.html',{'form':form,'title':title})  


def logout(request):
    auth.logout(request)
    return redirect('login/')

