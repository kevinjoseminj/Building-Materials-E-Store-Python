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
        result = Admin.objects.all()
        for x in result:
            if email in x.username:
                if password in x.password:
                    return render(request, 'adminhome.html')
                else:
                    return HttpResponse('Wrong password')
            else:
                return HttpResponse('Wrong username.')
    except Exception as e:
        return render(request, 'asign.html', {'m': 'An error occured'})