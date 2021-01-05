from django.db import models

# Create your models here.

class Customer(models.Model):
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    code = models.CharField(max_length=20)
    verified = models.CharField(max_length=20)
    
    class Meta:
        db_table = "Customer"

class Cart(models.Model):
    name  =  models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.CharField(max_length=100)

    class Meta:
        db_table = "Cart"

