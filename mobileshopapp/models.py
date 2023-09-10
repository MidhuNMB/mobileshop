from django.db import models
class useraccount_tbl(models.Model):
    username=models.CharField(max_length=500)
    firstname=models.CharField(max_length=500)
    email=models.CharField(max_length=500)
    phone=models.IntegerField()
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








# Create your models here.
