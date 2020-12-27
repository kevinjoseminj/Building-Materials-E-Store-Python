from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'home.html')

def login_form(request):
    return render(request, 'login.html')

def signup_form(request):
    return render(request, 'signup.html')


def cart(request):
    return render(request, 'cart.html')