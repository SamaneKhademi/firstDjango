from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models


def index(request):
    return render(request=request, template_name='index.html', context={})


def signUp(request):
    user=models.User(Email="s.khademi@gmail.com",Password="sa123456")
    user.save()
    return render(request=request, template_name='signUp.html',context={})

def datatabel(request):
    alldata=models.User.objects.all()
    return render(request=request, template_name='datatabel.html', context={"alldata":alldata})
