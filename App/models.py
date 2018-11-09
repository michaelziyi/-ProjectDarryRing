from django.db import models

# Create your models here.

class User(models.Model):
    phone = models.CharField(max_length=50)
    password = models.CharField(max_length=220)
    token = models.CharField(max_length=220)


class Goods(models.Model):
    id = models.CharField(max_length=8,primary_key=True)
    src = models.CharField(max_length=256)
    price = models.CharField(max_length=50)
    discript = models.CharField(max_length=256)
    sale = models.CharField(max_length=20)
    com = models.CharField(max_length=20)


class Wheel(models.Model):

    img = models.CharField(max_length=256)






