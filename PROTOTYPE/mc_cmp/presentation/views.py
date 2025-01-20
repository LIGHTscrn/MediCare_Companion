from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

def home_caregiver(request):
    return render(request, 'home_caregiver.html')

def home_elder(request):
    return render(request, 'home_elder.html')

def register(request):
    return render(request, 'register.html')
