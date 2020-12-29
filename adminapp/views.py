from django.shortcuts import render
from . models import Admin
from adminapp.models import *

# Create your views here.

def asign_in_form(request):
    return render(request, 'asign.html')


def ad_do_sign_in(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        result = Admin.objects.all()
        for x in result:
            if email in x.email:
                print(x.email)
                if password in x.password:
                    print(x.password)
                    return render(request, 'adminhome.html')
                else:
                    return HttpResponse('Wrong password')
            else:
                return HttpResponse('Wrong username.')
    except Exception as e:
        return render(request, 'asign.html', {'m': 'An error occured'})


def products(request):
    return render(request, 'aproducts.html')


def viewproducts(request):
    return render(request, 'viewproducts.html')


def viewdelete(request):
    return render(request, 'viewdelete.html')


def addproducts(request):
    return render(request,'addproducts.html')

