from django.shortcuts import render, redirect
from Productapp.models import Product
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import auth
from rest_framework import viewsets, permissions
from Productapp.serializers import UserSerializer
from rest_framework.decorators import MethodMapper, api_view
from rest_framework.response import Response
from django.http import HttpResponse, response

# Create your views here.
@login_required(login_url='login/')
def add_product(request):
    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('cost') and request.POST.get('currency') and request.POST.get('category') and request.POST.get('colour'):
            form = Product()
            form.name = request.POST.get('name')
            form.cost = request.POST.get('cost')
            form.currency = request.POST.get('currency')
            form.category = request.POST.get('category')
            form.colour = request.POST.get('colour')
            form.save()
    return render(request, 'index.html')

@login_required(login_url='login/')
def display(request):
    values=Product.objects.all()
    return render(request, "output.html", {'data':values})

def form(request):
    return render(request, 'forms.html')

def logout(request):
    auth.logout(request)
    return redirect('login/')

class UserViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
'''
@api_view(['GET'])
def get(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = UserSerializer(products,many=True)
        return Response(serializer.data)
'''
@api_view(['GET'])
def get(request):
    if request.method == 'GET':
        if(request.content_type=="application/json"):
            products = Product.objects.all()
            serializer = UserSerializer(products,many=True)
            return Response(serializer.data)
        elif(request.content_type=="text/html"):
            try: 
                products = Product.objects.all()  
            except:
                return HttpResponse("Something went wrong!")
            return render(request,"output.html",{"data":products})
'''
@api_view(['POST'])
def post(request):
    if request.method == 'POST':
        products = Product.objects.all()
        serializers = UserSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
        return render(request, "index.html", {"data":products})
        #return HttpResponse("Inserted Successfully!")
'''
@api_view(['POST'])
def post(request):
    if request.method == 'POST':
        products = Product.objects.all()
        if(request.content_type=="application/json"):
            serializer = UserSerializer(products,many=True)
            return Response(serializer.data)
            return render(request,"index.html",{"data":products})
        elif(request.content_type=="text/html"):
            try: 
                products = Product.objects.all()  
            except:
                return HttpResponse("Something went wrong!")
            return render(request,"index.html",{"data":products})

