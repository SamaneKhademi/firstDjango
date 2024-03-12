from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,),
    path('signUp/', views.signUp, name='ثبت نام'),
    path('datatabel/', views.datatabel, name='دیتاهای ثبت شده'),
    path('saveData/', views.saveData, name='ثبت دیتا'),
    path('edit/<int:id>', views.edit, name='ادیت دیتاهای ثبت شده'),
    path('editSave/<int:id>', views.editSave, name='ثبت دیتاهای ادیت شده'),
]
