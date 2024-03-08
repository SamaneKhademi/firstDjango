from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models
from . import form


def index(request):
    return render(request=request, template_name='index.html', context={})


def signUp(request):
    form1 = form.User()
    return render(request=request, template_name='formsignUp.html',context={'form':form1})

def datatabel(request):
    alldata=models.User.objects.all()
    return render(request=request, template_name='datatabel.html', context={"alldata":alldata})

def saveData(request):
    if request.method == 'POST':
        form2 = form.User(request.POST)
        if form2.is_valid():
            data = models.User(Email=form2.data['Email'], Password=form2.data['Password'])
            data.save()
            alldata = models.User.objects.all()
            return render(request=request, template_name='datatabel.html', context={"alldata":alldata})
