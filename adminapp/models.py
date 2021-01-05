from django.db import models

# Create your models here.

class Administrator(models.Model):
    email = models.CharField(max_length=50)
    password =  models.CharField(max_length=20)
    class Meta:
        db_table = "Administrator"

class Products(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    image = models.CharField(max_length=100)

    class Meta:
        db_table = "Products"

class Orders(models.Model):
    name = models.CharField(max_length=20)
    amount = models.IntegerField()
    address = models.CharField(max_length=100)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "Orders"

