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

    def __str__(self):
        return self.name

class Noodle(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/noodles")

    def __str__(self):
        return self.name
    
class Sisig(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/sisig")

    def __str__(self):
        return self.name

class Yangchow(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/yangchow")

    def __str__(self):
        return self.name

class Wing(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/wings")

    def __str__(self):
        return self.name

class Pork(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/pork")
    
    def __str__(self):
        return self.name


class Chicken(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/chicken")

    def __str__(self):
        return self.name

class Beef(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/beef")

    def __str__(self):
        return self.name

class Seafood(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/seafood")

    def __str__(self):
        return self.name

class Vegetable(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/vegetable")

    def __str__(self):
        return self.name

class Snack(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/snack")

    def __str__(self):
        return self.name

class Addon(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/addon")

    def __str__(self):
        return self.name

class Drink(Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    stock = models.IntegerField()
    imageURL = models.ImageField(upload_to="static/media/drinks")

    def __str__(self):
        return self.name
    
class Receipt(Model):
    name = models.CharField(max_length=255, default="customer")
    date = models.DateTimeField(default=datetime.datetime.now())
    items = models.TextField(default=" ")
    ref_num = models.CharField(max_length=10,editable=True, unique=True,default=create_new_ref_number())
    status = models.CharField(max_length=20,default="In Queue")

    def __str__(self):
        return " Ref: " + self.ref_num + " Date: " + str(self.date.astimezone().date()) + " Time: " + str(self.date.astimezone().time()) 
    
class CurrentTransaction(Model):
        items = models.CharField(max_length=255)
        itemcount = models.IntegerField()
        price = models.IntegerField()
        category = models.CharField(max_length=255, default='none')