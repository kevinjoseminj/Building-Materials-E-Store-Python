from django.shortcuts import render,redirect
from . models import Administrator,Products,Orders
from django.core.files.storage import FileSystemStorage

# Create your views here.

def asign_in_form(request):
    return render(request, 'asign.html')


def ad_do_sign_in(request):
    try:
        email = request.POST['email']
        password = request.POST['password']
        result = Administrator.objects.all()
        for x in result:
            if email in x.email:
                if password in x.password:
                    print(x.password)
                    order = Orders.objects.all()
                    return render(request, 'adminhome.html',{'order':order})  
                else:
                    return render(request, 'asign.html',{'m':'Wrong password'})
            else:
                return render(request, 'asign.html',{'m':'Wrong Username'})
    except Exception as e:
        return render(request, 'asign.html', {'m': 'An error occured'})


def products(request):
    return render(request, 'aproducts.html')


def addproducts(request):
    return render(request,'addproducts.html')


def saveproducts(request):
    proname = request.POST['productname']
    proprice = request.POST['price']
    proimage = request.FILES['productimage']
    fs = FileSystemStorage()
    photo = fs.save(proimage.name,proimage)
    fileurl = fs.url(photo)
    val=Products(name=proname, price=proprice, image=fileurl)
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
    proprice = request.POST['price']
    proimage = request.FILES['productimage']
    fs = FileSystemStorage()
    photo = fs.save(proimage.name,proimage)
    fileurl = fs.url(photo)
    Products.objects.filter(pk=id).update(name=proname,price=proprice,image=fileurl)
    return redirect('viewproducts')

def viewdelete(request):
    pro = Products.objects.all()
    return render(request,'viewdelete.html',{'pro':pro})

def deleteproduct(request,id):
    pro = Products.objects.get(id=id)
    pro.delete()
    return redirect('viewdelete')


def orderlist(request):
    order = Orders.objects.all()
    return render(request, 'adminhome.html',{'order':order})


def confirm(request,id):
    Orders.objects.filter(id=id).update(status="Delivered")
    return redirect('orderlist')

