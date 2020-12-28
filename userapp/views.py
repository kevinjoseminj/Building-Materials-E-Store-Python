from django.shortcuts import render
from . models import User

# Create your views here.

def home(request):
    return render(request,'home.html')

def login_form(request):
    return render(request, 'login.html')

def signup_form(request):
    return render(request, 'signup.html')

def cart(request):
    return render(request, 'cart.html')

def do_sign_up(request):
    try:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        myresult=User.objects.all()
        f = True
        for x in myresult:
            if email in x.email:
                f = False
        if f:
            val = User(username=username, email=email, password=password)
            val.save()
            return render(request,'login.html',{'m':'Successfully created account'})
        else:
            return render(request, 'signup.html', {'m': 'You entered an existing username.'})
    except Exception as e:
        print(e)
        return render(request, 'signup.html', {'m':'An error occured'})

def do_sign_in(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        result = User.objects.all()
        for x in result:
            if email in x.email:
                if password in x.password:
                    return render(request, 'cart.html')
                else:
                    return HttpResponse('Wrong password')
            else:
                return HttpResponse('Wrong username.')
    except Exception as e:
        return render(request, 'login.html', {'m': 'An error occured'})