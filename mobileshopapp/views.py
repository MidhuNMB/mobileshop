from django.shortcuts import render,redirect
def index(request):
    # return render(request,'index.html')
    # return render(request,'admin.html')
    return render(request,'staff.html')
    # return render(request,'user.html')
def createuser(request):
    return render(request,'createuser.html')
def loginuser(request):
    return render(request,'loginuser.html')
def index2(request):
    return render(request,'index.html')
def index1(request):
    return render(request,'index.html')
# Create your views here.
