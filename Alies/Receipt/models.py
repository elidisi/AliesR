from django.db.models import Model
from django.db import models
from .utils import create_new_ref_number

class Receipt(Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    items = models.TextField()
    ref_num = models.CharField(max_length=10, editable=False, unique=True, default=create_new_ref_number())
    
class CurrentTransaction(Model):
        items = models.CharField(max_length=255)
        itemcount = models.IntegerField()
        price = models.IntegerField()

        
