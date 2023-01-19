from django.shortcuts import render, redirect
from django.conf import settings
from .models import Contact


def index(request):
    data = Contact.objects.all()
    print(data)

    context = {"data": data}

    return render(request,"index.html",context)



def insertData(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        name=request.POST.get('name')
        sem=request.POST.get('sem')
        mobno=request.POST.get('mobno')
        print(uname,name,sem,mobno)
        query=Contact(uname=uname,name=name,sem=sem,mobno=mobno)
        query.save()
        return redirect('/')
    return render(request,"index.html")

def updateData(request,uname):
    edit = Contact.objects.get(uname=uname)
    if request.method == "POST":
        name = request.POST['name']
        sem = request.POST['sem']
        mobno = request.POST['mobno']

        edit.name=name
        edit.sem=sem
        edit.mobno=mobno
        edit.save()


        return redirect('/')

    d = Contact.objects.get(uname=uname)

    context = {"d": d}

    return render(request,"edit.html",context)

def deleteData(request,uname):
    data = Contact.objects.get(uname=uname)
    data.delete()
    return redirect('index')
    return render(request,"index.html")


