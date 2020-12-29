from django.shortcuts import render
from . models import Customer
from random import randint
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def random_with_N_digits(n):
	range_start = 10**(n-1)
	range_end = (10**n)-1
	return randint(range_start,range_end)


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
        code = random_with_N_digits(6)
        myresult=Customer.objects.all()
        f = True
        for x in myresult:
            if email in x.email:
                f = False
        if f:
            val = Customer(username=username, email=email, password=password, code=code,verified='pending')
            subject = 'Confirmation Mail'
            message = ' Your Confirmation code is '+str(code)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list )
            val.save()
            return render(request, 'verify.html',{'msg':'Request Sent'})
        else:
            return render(request, 'signup.html', {'m': 'You entered an existing username.'})
    except Exception as e:
        print(e)
        return render(request, 'signup.html', {'m':'An error occured'})

def otpverify(request):
    otp = request.POST['otp']
    codeid = Customer.objects.last()
    code = codeid.code
    if otp==code:
        codeid.verified = 'verified'
        codeid.save()
        return render(request, 'userhome.html')
    else:
        return render(request,'cverify.html',{'msg':'Entered wrong OTP'})
            
    
def do_sign_in(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        result = Customer.objects.all()
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


