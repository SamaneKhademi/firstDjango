from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models
from . import form
import socket

def index(request):
    return render(request=request, template_name='index.html', context={})


def signUp(request):
    form1 = form.Userform()
    return render(request=request, template_name='formsignUp.html', context={'form': form1})


def datatabel(request):
    alldata = models.User.objects.all()
    return render(request=request, template_name='datatabel.html', context={"alldata": alldata})


def saveData(request):
    host=socket.gethostname()
    ip=socket.gethostbyname(host)
    if request.method == 'POST':
        form2 = form.Userform(request.POST)
        if form2.is_valid():
            data = models.User(ip=ip, Email=form2.data['Email'], Password=form2.data['Password'])
            data.save()
            alldata = models.User.objects.all()
            return render(request=request, template_name='datatabel.html', context={"alldata": alldata})


def edit(request, id):
    data1 = models.User.objects.filter(id=id).first()
    form2 = form.Userform(initial={'Email': data1.Email, 'Password':data1.Password})
    return render(request=request, template_name='edit.html', context={'form': form2, 'id': id})


def editSave(request, id):
    if request.method == 'POST':
        data1 = models.User.objects.filter(id=id).first()
        form2 = form.Userform(request.POST)
        data1.Email= form2.data['Email']
        data1.Password= form2.data['Password']
        data1.save()
        alldata = models.User.objects.all()
        return render(request=request, template_name='datatabel.html', context={"alldata": alldata})







