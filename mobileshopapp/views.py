from django.shortcuts import render,redirect
from mobileshopapp.models import user_tbl,useraccount_tbl,staff_tbl,seller_tbl
from django. contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
def index(request):
    #return render(request,'index.html')
    return render(request,'admin.html')
    # return render(request,'staff.html')
    # return render(request,'user.html')
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
    a.first_name=request.POST.get('fistname')
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
    b.photo=request.POST.get('photo')
    b.username=request.POST.get('username')

    c.username=request.POST.get('username')
    c.firstname=request.POST.get('firstname')
    c.email=request.POST.get('email')
    b.phone=request.POST.get('phone')
    c.accounttype="user"

    a.save()
    b.save()
    c.save()
    return redirect('/')
def createac(request):
    c=useraccount_tbl()
    d=seller_tbl()
    e=staff_tbl()
    c.firstname=request.POST.get('firstname')
    c.accounttype="user"
    c.email=request.POST.get('email')
    c.phone=request.POST.get('phone')
    c.accounttype=request.POST.get('accounttype')
    a.save()
    b.save()
    c.save()
    return redirect('/')
def login1(request):
    a=request.POST.get('username')
    b=request.POST.get('password')
    data=authenticate(username=a,password=b)
    if data is not None and data.is_superuser==1:
        return redirect('/admin/')
    elif data is not None and data.is_superuser==0:
        return redirect('/user/')
    else:
        return HttpResponse('invalid login')
def admin1(request):
    return render(request,'admin.html')
def user1(request):
    return render(request,'user.html')

    


    
# Create your views here.
