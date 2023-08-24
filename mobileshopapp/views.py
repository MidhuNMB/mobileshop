from django.shortcuts import render,redirect
def index(request):
    return render(request,'index.html')
def createuser(request):
    return render(request,'createuser.html')
def loginuser(request):
    return render(request,'loginuser.html')
def index2(request):
    return render(request,'index.html')
# Create your views here.
