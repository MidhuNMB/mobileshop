from django.shortcuts import render,redirect
from mobileshopapp.models import user_tbl,useraccount_tbl,staff_tbl,seller_tbl
from django. contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
def index(request):
    return render(request,'index.html')
   
def createuser(request):
    return render(request,'createuser.html')
def loginuser(request):
    return render(request,'loginuser.html')
def index2(request):
    return render(request,'index.html')
def index1(request):
    return render(request,'index.html')


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
    return redirect('/loginuser/')

def createsellerac(request):
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
    c.accounttype="seller"

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
    return redirect('/adminHome/')

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
    return redirect('/adminHome/')
    
def login1(request):
    username=request.POST.get('username')
    b=request.POST.get('password')
    data=authenticate(username=username,password=b)
    request.session['username']=username

    if data is not None and data. is_superuser==1:
        return redirect('/adminHome/')
    elif data is not None and data.is_superuser==0:
        d1=useraccount_tbl.objects.get(username=data)
        if d1.accounttype=="user":
            return redirect('/userHome/')
        elif d1.accounttype=="seller":
            return redirect('/sellerpg/')
        elif d1.accounttype=="staff":
            return redirect('/staffpg/')
    else:
        return HttpResponse('invalid login')
    
def adminHome(request):
    return render(request,'admin.html')
def userHome(request):
    return render(request,'user.html')
def staffHome(request):
    return render(request,'createstaff.html')
def sellerHome(request):
    return render(request,'createseller.html')
def viewseller(request):
    return render(request,'viewseller.html')
def staffpg(request):
    return render(request,'staffpg.html')
def sellerpg(request):
    return render(request,'sellerpg.html')

def viewseller(request):
   a=seller_tbl.objects.all()
   return render(request,'viewseller.html',{'data':a})
def delete1(request,id):
    a=seller_tbl.objects.get(id=id)
    a.delete()
    return redirect('/viewseller/',{'data':a})

def viewstaff(request):
    return render(request,'viewstaff.html')
def viewstaff(request):
    a=staff_tbl.objects.all()
    return render(request,'viewstaff.html',{'data':a})
def delete2(request,id):
    a=staff_tbl.objects.get(id=id)
    a.delete()
    return redirect('/viewstaff/',{'data':a})




# please check
#def viewuserprofile(request):
    #a=request.session['username']
    #return render(request,'viewuserprofile.html',{'a1':a})
#def viewpro(request):
   # a=request.session['username']
   # a1=user_tbl.objects.get(username=a)
    #return render(request,'viewuserprofile.html',{'a1':a1})
def viewuserprofile(request):
    a = request.session['username']
    a1 = user_tbl.objects.get(username=a)
    return render(request, 'viewuserprofile.html', {'a1': a1})

#def updateseller(request,id):
   #return render(request,'updateseller.html')








def update1(request,id):
    a=seller_tbl.objects.get(id=id)
    return render(request,'updateseller.html',{'data':a})
def updatesellerac(request,id):
    d=seller_tbl(id=id)
   
    d.firstname=request.POST.get('firstname')
    d.lastname=request.POST.get('lastname')
    d.gender=request.POST.get('gender')
    d.email=request.POST.get('email')
    d.phone=request.POST.get('phone')
    d.address=request.POST.get('address')
    d.district=request.POST.get('district')
    d.photo=request.FILES['photo']
    d.username=request.POST.get('username')
    d.save()
    return redirect('/viewseller/')

def update2(request,id):
    a=staff_tbl.objects.get(id=id)
    return render(request,'updatestaff.html',{'data':a})

def updatestaffac(request,id):
    d=staff_tbl.objects.get(id=id)

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
    d.save()
    return redirect('/viewstaff/')

def logout(request):
    return render(request,'index.html')

def viewsellerprofile(request):

    a = request.session['username']
    a1 = seller_tbl.objects.get(username=a)
    return render(request, 'viewsellerprofile.html', {'a1':a1})
    





  
# Create your views here.