from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Customer,Cart
from adminapp.models import *
from random import randint
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Sum
import razorpay

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
    cart = Cart.objects.all()
    cart_item_count = Cart.objects.count()
    return render(request, 'cart.html',{'cart':cart,'cart_item_count':cart_item_count})

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
        return redirect('userhome')
    else:
        return render(request,'cverify.html',{'msg':'Entered wrong OTP'})


def userhome(request):
    pro = Products.objects.all()
    return render(request, 'userhome.html',{'pro':pro})      
    

def do_sign_in(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        result = Customer.objects.all()
        for x in result:
            if email in x.email:
                if password in x.password:
                    return redirect('userhome')
                else:
                    return HttpResponse('Wrong password')
            else:
                return HttpResponse('Wrong username.')
    except Exception as e:
        return render(request, 'login.html', {'m': 'An error occured'})

def add_to_cart(request,id):
    pro = Products.objects.get(id=id)
    val=Cart(name=pro.name, description=pro.description, price=pro.price, image=pro.image)
    val.save()
    return redirect('userhome')

def placeorder(request):
    return render(request, 'placeorder.html')

def checkout(request):
    Username = request.POST['Username']
    Address = request.POST['Address']
    State = request.POST['State']
    ziip = request.POST['zip']
    a={}
    if request.POST['paymentMethod']=='COD':
        for i in ["Username", "Address", "State", "ziip"]:
            a[i] = eval(i)
        return render(request, 'ordersuccess.html', {'a':a})
    else:
        name = Username 
        total= Cart.objects.annotate(total=Sum('price'))
        summ=0
        for i in total:
            summ+=i.price
        print(summ)
        amount = summ
        client = razorpay.Client(auth=("rzp_test_BxZvEpl01zwGtx","YI8wYJqkAXi7vGiTUcOSaOgN"))
        payment = client.order.create({'amount': amount, 'currency': 'INR','payment_capture': '1'})
        print(payment)
        return render(request, 'payment.html',{'payment':payment,'name':name})

def success(request):
    return render(request, "success.html")
        
    

        
        








