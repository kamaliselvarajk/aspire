from django.urls import path, include
from demoapp import views

urlpatterns = [
    path('newuser/', views.create_user),
    path('showuser/', views.list_user),
]