from django.shortcuts import render, redirect
from .models import emp

# Create your views here.
def index(request):
    mem = emp.objects.all()
    return render(request,'index.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addemp(request):
    a=request.POST['fullname']
    b=request.POST['contactno']
    c=request.POST['emailid']
    d=request.POST['dateofbirth']
    e=request.POST['gender']
    f=request.POST['jobrole']
    g=request.POST['address']
    mem=emp(fullname=a,contactno=b,emailid=c,dateofbirth=d,gender=e,jobrole=f,address=g)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=emp.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=emp.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    a=request.POST['fullname']
    b=request.POST['contactno']
    c=request.POST['emailid']
    d=request.POST['dateofbirth']
    e=request.POST['gender']
    f=request.POST['jobrole']
    g=request.POST['address']
    mem=emp.objects.get(id=id)
    mem.fullname=a
    mem.contactno=b
    mem.emailid=c
    mem.dateofbirth=d
    mem.gender=e
    mem.jobrole=f
    mem.address=g
    mem.save()
    return redirect("/")