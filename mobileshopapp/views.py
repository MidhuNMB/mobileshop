from django.shortcuts import render,redirect
from mobileshopapp.models import user_tbl,staff_tbl,seller_tbl,useraccount_tbl
from django. contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')
    #return render(request,'admin.html')
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
def createac(request):
    a=User()
    b=user_tbl()
    a.first_name=request.POST.get('fistname')
    a.last_name=request.POST.get('lastname')
    a.username=request.POST.get('username')
    password=request.POST.get('password')
    a,b.set_password(password)
    b.firstname=request.POST.get('firstname')
    b.lastname=request.post.get('lastname')
    b.gender=request.POST.get('gender')
    b.email=request.POST.get('email')
    b.phone=request.POST.get('phone')
    b.address=request.POST.get('address')
    b.district=request.POST.get('district')
    b.photo=request.POST.get('photo')
    b.username=request.POST.get('username')
    a.save()
    b.save()
    return redirect('/')
    


    
# Create your views here.
