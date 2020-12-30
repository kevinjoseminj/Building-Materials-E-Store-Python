from django.shortcuts import render,redirect
from . models import Administrator
from adminapp.models import *
from django.core.files.storage import FileSystemStorage

# Create your views here.

def asign_in_form(request):
    return render(request, 'asign.html')


def ad_do_sign_in(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        result = Administrator.objects.all()
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


"""def viewproducts(request):
    return render(request, 'viewproducts.html')"""


def viewdelete(request):
    return render(request, 'viewdelete.html')


def addproducts(request):
    return render(request,'addproducts.html')


def saveproducts(request):
    proname = request.POST['productname']
    proddescription = request.POST['description']
    proprice = request.POST['price']
    prostock = request.POST['stock']
    proimage = request.FILES['productimage']
    fs = FileSystemStorage()
    photo = fs.save(proimage.name,proimage)
    fileurl = fs.url(photo)
    val=Products(name=proname, description=proddescription, price=proprice, stock=prostock, image=fileurl)
    val.save()
    return redirect('addproducts')


def viewproducts(request):
    pro = Products.objects.all()
    return render(request,'viewproducts.html',{'pro':pro})


def editproduct(request,id):
    pro = Products.objects.get(id=id)
    return render(request, 'editproduct.html',{'pro':pro})


def updateproduct(request,id):
    pro = Products.objects.get(id=id) 
    proname = request.POST['productname']
    proddescription = request.POST['description']
    proprice = request.POST['price']
    prostock = request.POST['stock']
    proimage = request.FILES['productimage']
    fs = FileSystemStorage()
    photo = fs.save(proimage.name,proimage)
    fileurl = fs.url(photo)
    Products.objects.filter(pk=id).update(name=proname, description=proddescription, price=proprice, stock=prostock, image=fileurl)
    return redirect('viewproducts')



