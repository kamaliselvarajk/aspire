from django.urls import path
from . import views

urlpatterns = [
    path('userform/', views.register, name='register'),
    path('userform/login/', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('logout/login/', views.login, name='logout'),
    path('userform/login/show/logout/', views.login, name='logout'),

]