from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,),
    path('signUp/', views.signUp, name='ثبت نام'),
]
