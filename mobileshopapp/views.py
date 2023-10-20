from django.shortcuts import render,redirect
from mobileshopapp.models import user_tbl,useraccount_tbl,staff_tbl,seller_tbl,product_tbl,cart_tbl
from django. contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

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
    photo=request.FILES['photo']
    fs=FileSystemStorage()
    image=fs.save(photo.name,photo)
    image1=fs.url(image)
    b.photo=image1
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
    photo=request.FILES['photo']
    fs=FileSystemStorage()
    image=fs.save(photo.name,photo)
    image1=fs.url(image)
    d.photo=image1
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
    photo=request.FILES['photo']
    fs=FileSystemStorage()
    image=fs.save(photo.name,photo)
    image1=fs.url(image)
    d.photo=image1
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
    a = request.session['username']
    a1 = user_tbl.objects.get(username=a)
    return render(request,'user.html',{'x':a1})

def staffHome(request):
   
    return render(request,'createstaff.html')
def sellerHome(request):
    
    return render(request,'createseller.html')
def viewseller(request):
    return render(request,'viewseller.html')
def staffpg(request):
    return render(request,'staffpg.html')
def sellerpg(request):
    a = request.session['username']
    a1 = seller_tbl.objects.get(username=a)
    return render(request,'sellerpg.html',{'x':a1})

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
    b=useraccount_tbl.objects.get(username=a.username)
    c=User.objects.get(username=a.username)
    a.delete()
    b.delete()  
    c.delete()
    return redirect('/loginuser/',{'data':a})

def deleteSeller(request,id):
    a=seller_tbl.objects.get(id=id)
    b=useraccount_tbl.objects.get(username=a.username)
    c=User.objects.get(username=a.username)

    a.delete()
    b.delete()
    c.delete()
    return redirect('/')



def viewuserprofile(request):
    a = request.session['username']
    a1 = user_tbl.objects.get(username=a)
    return render(request, 'viewuserprofile.html', {'a1': a1})
def update1(request,id):
    a=seller_tbl.objects.get(id=id)
    return render(request,'updateseller.html',{'data':a})

def updatesellerac(request,id):
    d=seller_tbl.objects.get(id=id)
    try:
        d.firstname=request.POST.get('firstname')
        d.lastname=request.POST.get('lastname')
        d.email=request.POST.get('email')
        d.phone=request.POST.get('phone')
        d.address=request.POST.get('address')
        d.district=request.POST.get('district')
        photo=request.FILES['photo']
        fs=FileSystemStorage()
        image=fs.save(photo.name,photo)
        image1=fs.url(image)
        d.photo=image1
        
        d.save()
    except:    
        d.firstname=request.POST.get('firstname')
        d.lastname=request.POST.get('lastname')
       
        d.email=request.POST.get('email')
        d.phone=request.POST.get('phone')
        d.address=request.POST.get('address')
        d.district=request.POST.get('district')
       
       
        d.save()
    return redirect('/viewsellerprofile/')

def update2(request,id):
    a=staff_tbl.objects.get(id=id)
    return render(request,'updatestaff.html',{'data':a})


def updatestaffac(request,id):
    d=staff_tbl.objects.get(id=id)
    try:

        d.firstname=request.POST.get('firstname')
        d.lastname=request.POST.get('lastname')
        d.designation=request.POST.get('designation')
        d.age=request.POST.get('age')
        d.gender=request.POST.get('gender')
        d.email=request.POST.get('email')
        d.phone=request.POST.get('phone')
        d.address=request.POST.get('address')
        d.district=request.POST.get('district')
        photo=request.FILES['photo']
        fs=FileSystemStorage()
        image=fs.save(photo.name,photo)
        image1=fs.url(image)
        d.photo=image1
        d.username=request.POST.get('username')
        d.save()
    except:
        d.firstname=request.POST.get('firstname')
        d.lastname=request.POST.get('lastname')
        d.designation=request.POST.get('designation')
        d.age=request.POST.get('age')
        d.gender=request.POST.get('gender')
        d.email=request.POST.get('email')
        d.phone=request.POST.get('phone')
        d.address=request.POST.get('address')
        d.district=request.POST.get('district')

    return redirect('/viewstaffpro/')

def logout(request):
    return render(request,'index.html')

def viewsellerprofile(request):

    a = request.session['username']
    a1 = seller_tbl.objects.get(username=a)
    return render(request, 'viewsellerprofile.html', {'a1':a1})
    
def viewstaffpro(request):
    a=request.session['username']
    a1=staff_tbl.objects.get(username=a)
    return render(request,'viewstaffprofile.html',{'a1':a1})



def updateuser(request,id):
    a1=user_tbl.objects.get(id=id)
    return render(request,'updateuser.html',{'a1':a1})

def updateuserac(request,id):
    b=user_tbl.objects.get(id=id)

    try:
        b.firstname=request.POST.get('firstname')
        b.lastname=request.POST.get('lastname')
        b.gender=request.POST.get('gender')
        b.email=request.POST.get('email')
        b.phone=request.POST.get('phone')
        b.address=request.POST.get('address')
        b.district=request.POST.get('district')
        photo=request.FILES['photo']
        fs=FileSystemStorage()
        image=fs.save(photo.name,photo)
        image1=fs.url(image)
        b.photo=image1
        
        b.save()
    except: 
           
        b.firstname=request.POST.get('firstname')
        b.lastname=request.POST.get('lastname')
        b.gender=request.POST.get('gender')
        b.email=request.POST.get('email')
        b.phone=request.POST.get('phone')
        b.address=request.POST.get('address')
        b.district=request.POST.get('district')
       
        b.save()
    return redirect('/userHome/')

def deleteuser(request,id):
    a=user_tbl.objects.get(id=id)
    b=User.objects.get(username=a.username)
    c=useraccount_tbl.objects.get(username=a.username)
    a.delete()
    b.delete()
    c.delete()
    return redirect('/loginuser/',{'a1':a})

def addproduct(request):
    a=request.session['username']
    return render( request,'addproduct.html',{'a':a})
def addprotbl(request):
    a=product_tbl()
    a.brandname=request.POST.get('brandname')
    photo=request.FILES['photo']
    fs=FileSystemStorage()
    image=fs.save(photo.name,photo)
    image1=fs.url(image)
    a.photo=image1
    a.colour=request.POST.get('colour')
    a.description=request.POST.get('description')
    a.price=request.POST.get('price')
    a.modelname=request.POST.get('modelname')
    a.batetrystatus=request.POST.get('bs')
    a.sellername=request.POST.get('sellername')
    
    a.save()
    return redirect('/addproduct/')
def viewprod(request):
    return render(request,'viewproduct.html')
def viewprod(request):
    a=product_tbl.objects.all()
    return render(request,'viewproduct.html',{'data':a})

def updateproduct(request,id):
    a=product_tbl.objects.get(id=id)
    return render(request,'updateproduct.html',{'data':a})

def updateprotbl(request,id):
    a=product_tbl.objects.get(id=id)
    try:
        a.brandname=request.POST.get('brandname')
        photo=request.FILES['photo']
        fs=FileSystemStorage()
        image=fs.save(photo.name,photo)
        image1=fs.url(image)
        a.photo=image1
        a.colour=request.POST.get('colour')
        a.description=request.POST.get('description')
        a.price=request.POST.get('price')
        a.batetrystatus.POST.get('batterystatus')
    except:
        a.brandname=request.POST.get('name')
        a.colour=request.POST.get('colour')
        a.description=request.POST.get('description')
        a.price=request.POST.get('price')
        a.modelname=request.POST.get('modelname')
        a.batetrystatus=request.POST.get('batterystatus')

        a.save()
        return redirect('/viewproduct/')
def deletepro(request,id):
    a=product_tbl.objects.get(id=id)
    a.delete()
    return redirect('/viewproduct/',{'data':a})

#def cartpg(request):
    return render(request,'cart.html')

#def addtocart(request,id):
    if request.user.is_authenticated():
            try:
                book = Book.objects.get(id=id)
            except ObjectDoesNotExist:
                pass
            else :
                try:
                    cart = Cart.objects.get(user = request.user, active = True)
                except ObjectDoesNotExist:
                    cart = Cart.objects.create(user = request.user)
                    cart.save()
                    cart.add_to_cart(book_id)
                    return redirect('cart')
                else:
                    return redirect('index')
                
def addtocart(request,id):
    un=request.session['username']
    a=product_tbl.objects.get(id=id)
    return render(request,'cart.html',{'a1':a,"user":un})
# def viewcart(request):

def usrprtbl(request,id):
    a=product_tbl.objects.all(id=id)
    return render(request,'user.html',{'a':a})
def adcrtbl(request):
    a=cart_tbl()
    b=request.POST.get('id')
    print(b,"Daata")
    c=product_tbl.objects.get(id=b)
    a.username=request.POST.get('username')
    a.productname=request.POST.get('productname')
    a.brand=c.brandname
    print(a.productname,"test1")
    a.sellername=request.POST.get('sellername')
    a.quantity=request.POST.get('quantity')
    a.price=request.POST.get('price')
    a.satus="in cart"
    a.totalAmount=int(a.quantity)*int(a.price)
    a.photo=c.photo
    a.save()
    return redirect('/viewproduct/')








  
# Create your views here.