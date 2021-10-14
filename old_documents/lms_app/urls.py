from django.urls import path
from . import views
#from Productapp.views import input_form

urlpatterns = [
    path('add/', views.user_profile, name='adduser'),
    path('approve/', views.approve_leave, name='approve'),
    path('apply/', views.leave_request, name='leave_request'),
    path('splogin/', views.user_login, name='login'),
    path('splogout/', views.logout_view, name='logout'),
    path('leavestatus/', views.view_approve_details, name='leave_status'),
    #path('leavedetails/', views.view_leave_details, name='leave_status'),
]