from django.db.models import Model
from django.db import models
from .utils import *
from django.http import HttpResponse
import datetime

class Breakfast(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/breakfast")

class Noodle(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/noodles")
    
class Sisig(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/sisig")

class Yangchow(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/yangchow")

class Wing(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/wings")

class Pork(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/pork")


class Chicken(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/chicken")

class Beef(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/beef")

class Seafood(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/seafood")

class Vegetable(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/vegetable")

class Snack(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/snack")

class Addon(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/addon")

class Drink(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/drinks")
    
class Receipt(Model):
    name = models.CharField(max_length=255, default="customer")
    date = models.DateTimeField(default=datetime.datetime.now())
    items = models.TextField(default=" ")
    ref_num = models.CharField(max_length=10,editable=True, unique=True,default=create_new_ref_number())
    status = models.CharField(max_length=20,default="In Queue")
    
class CurrentTransaction(Model):
        items = models.CharField(max_length=255)
        itemcount = models.IntegerField()
        price = models.IntegerField()