from django.urls import path
from . import views
#from Productapp.views import input_form

urlpatterns = [
    path('leave/', views.add_emp_leave, name='index'),
    path('pl/', views.pl, name='leave'),
    path('cl/', views.cl, name='leave'),
    path('cf/', views.cf, name='leave'),
    #path('lt/', views.leave_type, name='leave'),
]