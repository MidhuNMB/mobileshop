from django.db import models
class useraccount_tbl(models.Model):
    username=models.CharField(max_length=500)
    firstname=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    accounttype=models.CharField(max_length=500)
    class meta:
        db_tbl='useraccount_tbl'
class user_tbl(models.Model):
    firstname=models.CharField(max_length=500)
    lastname=models.CharField(max_length=500)
    gender=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    phone=models.IntegerField()
    address=models.CharField(max_length=500)
    district=models.CharField(max_length=500)
    photo=models.CharField(max_length=5000)
    username=models.CharField(max_length=500)
    password=models.CharField(max_length=500)
    class meta:
        db_tbl='user_tbl'
class seller_tbl(models.Model):
    firstname=models.CharField(max_length=500)
    lastname=models.CharField(max_length=500)
    gender=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    phone=models.IntegerField()
    address=models.CharField(max_length=500)
    district=models.CharField(max_length=500)
    photo=models.CharField(max_length=5000)
    username=models.CharField(max_length=500)
    class meta:
        db_tbl='seller_tbl'
class staff_tbl(models.Model):
    firstname=models.CharField(max_length=500)
    lastname=models.CharField(max_length=500)
    designation=models.CharField(max_length=500)
    age=models.CharField(max_length=500)
    gender=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    phone=models.IntegerField()
    address=models.CharField(max_length=500)
    district=models.CharField(max_length=500)
    photo=models.CharField(max_length=500)
    username=models.CharField(max_length=500)
    class meta:
        db_tbl='staff_tbl'

class product_tbl(models.Model):
    sellername=models.CharField(max_length=500)
    brandname=models.CharField(max_length=500)
    modelname=models.CharField(max_length=500)
    colour=models.CharField(max_length=500)
    description=models.CharField(max_length=500)
    price=models.CharField(max_length=500)
    batetrystatus=models.CharField(max_length=500)
    photo=models.CharField(max_length=50)
    class meta:
        db_tbl='product_tbl'

class cart_tbl(models.Model):
    username=models.CharField(max_length=500)
    photo=models.CharField(max_length=500)
    productname=models.CharField(max_length=500)
    brand=models.CharField(max_length=500)
    sellername=models.CharField(max_length=500)
    quantity=models.IntegerField()
    price=models.IntegerField()
    satus=models.CharField(max_length=500)
    totalAmount=models.IntegerField()

    class meta:
        db_tbl='cart_tbl'









# Create your models here.
