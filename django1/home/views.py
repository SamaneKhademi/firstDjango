from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models


def index(request):
    return render(request=request, template_name='index.html', context={})


def signUp(request):
    page1=loader.get_template('signUp.html')
    context={}
    return HttpResponse(page1.render())



    """
    user1=models.user(name="samane", email="s.khademi1992@gmail.com", password="123456")
    user1.save()
    context={"user":user1}
    return HttpResponse(page1.render(context))
"""