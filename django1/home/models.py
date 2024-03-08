from django.db import models

# Create your models here.

class User(models.Model):
    Email = models.CharField(max_length=50)
    Password = models.CharField(max_length=15)