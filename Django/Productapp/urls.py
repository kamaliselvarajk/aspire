from django.urls import path
from . import views
#from Productapp.views import input_form

urlpatterns = [
    path('add/', views.add_product, name='index'),
    path('show/', views.display, name='display'),
    path('userform/login/show/', views.display, name='display'),
    path('userform/login/show/add/', views.add_product, name='index'),
]