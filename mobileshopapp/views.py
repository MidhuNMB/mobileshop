from django.shortcuts import render,redirect
from mobileshopapp.models import user_tbl,useraccount_tbl,staff_tbl,seller_tbl
from django. contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
def index(request):
    #return render(request,'index.html')
    #return render(request,'admin.html')
    # return render(request,'staff.html')
    # return render(request,'user.html')
    #return render(request,'seller.html')
    return render(request,'viewseller.html')
def createuser(request):
    return render(request,'createuser.html')
def loginuser(request):
    return render(request,'loginuser.html')
def index2(request):
    return render(request,'index.html')
def index1(request):
    return render(request,'index.html')
def staffpg(request):
    return render(request,'staff.html')
def sellerpg(request):
    return render(request,'seller.html')

def createac1(request):
    a=User()
    b=user_tbl()
    c=useraccount_tbl()
    a.first_name=request.POST.get('firstname')
    a.last_name=request.POST.get('lastname')
    a.username=request.POST.get('username')
    password=request.POST.get('password')
    a.set_password(password)

    b.firstname=request.POST.get('firstname')
    b.lastname=request.POST.get('lastname')
    b.gender=request.POST.get('gender')
    b.email=request.POST.get('email')
    b.phone=request.POST.get('phone')
    b.address=request.POST.get('address')
    b.district=request.POST.get('district')
    b.photo=request.FILES['photo']
    b.username=request.POST.get('username')

    c.username=request.POST.get('username')
    c.firstname=request.POST.get('firstname')
    c.email=request.POST.get('email')
    c.accounttype="user"

    a.save()
    b.save()
    c.save()
    return redirect('/')

def createsa(request):
    d=seller_tbl()
    a=User()
    c=useraccount_tbl()

    a.first_name=request.POST.get('firstname')
    a.last_name=request.POST.get('lastname')
    a.username=request.POST.get('username')
    password=request.POST.get('password')
    a.set_password(password)

    c.username=request.POST.get('username')
    c.firstname=request.POST.get('firstname')
    c.email=request.POST.get('email')
    c.accounttype="seler"

    d.firstname=request.POST.get('firstname')
    d.lastname=request.POST.get('lastname')
    d.gender=request.POST.get('gender')
    d.email=request.POST.get('email')
    d.phone=request.POST.get('phone')
    d.address=request.POST.get('address')
    d.district=request.POST.get('district')
    d.photo=request.FILES['photo']
    d.username=request.POST.get('username')
    a.save()
    c.save()
    d.save()
    return redirect('/')

def createstaffac(request):
    d=staff_tbl()
    a=User()
    c=useraccount_tbl()
    
    a.first_name=request.POST.get('firstname')
    a.last_name=request.POST.get('lastname')
    a.username=request.POST.get('username')
    password=request.POST.get('password')
    a.set_password(password)

    c.username=request.POST.get('username')
    c.firstname=request.POST.get('firstname')
    c.email=request.POST.get('email')
    c.accounttype="staff"

    d.firstname=request.POST.get('firstname')
    d.lastname=request.POST.get('lastname')
    d.designation=request.POST.get('designation')
    d.age=request.POST.get('age')
    d.gender=request.POST.get('gender')
    d.email=request.POST.get('email')
    d.phone=request.POST.get('phone')
    d.address=request.POST.get('address')
    d.district=request.POST.get('district')
    d.photo=request.FILES['photo']
    d.username=request.POST.get('username')
    a.save()
    c.save()
    d.save()
    return redirect('/')
    
def login1(request):
    a=request.POST.get('username')
    b=request.POST.get('password')
    data=authenticate(username=a,password=b)

    if data is not None and data. is_superuser==1:
        return redirect('/admin/')
    elif data is not None and data.is_superuser==0:
        return redirect('/user/')
    else:
        return HttpResponse('invalid login')
def admin(request):
    return render(request,'admin.html')
def user(request):
    return render(request,'user.html')
def viewseller(request):
    return render(request,'viewseller.html')



    


    
# Create your views here.

    



    


    
# Create your views here.
