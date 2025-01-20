from django.urls import path
from . import views

urlpatterns = [
    path('/login', views.login, name='login'),
    path('', views.register, name='register'),
    path('/home_caregiver', views.home_caregiver, name='home_caregiver'),
    path('/home_elder', views.home_elder, name='home_elder'),
]