from django.db import models

# Create your models here.

class Administrator(models.Model):
    email = models.CharField(max_length=50)
    password =  models.CharField(max_length=20)

class Products(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    stock = models.IntegerField()
    image = models.CharField(max_length=100)

class Orders(models.Model):
    name = models.CharField(max_length=20)
    amount = models.IntegerField()
    address = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

