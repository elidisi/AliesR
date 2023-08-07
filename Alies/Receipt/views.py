from django.http import HttpResponse
from django.template import loader
from .models import *

def dashboard(request):
    context = {
        'breakfast': Breakfast.objects.all()
    }
    
    form = loader.get_template("GUI/dashboard.html") 
    return HttpResponse(form.render(context,request))

def login(request):
    form = loader.get_template("GUI/login.html")
    return HttpResponse(form.render({},request))

def order(request):
    context = {
        "breakfast":Breakfast.objects.all(),
    }

    form = loader.get_template("GUI/order.html") 
    return HttpResponse(form.render(context,request))

def checkout(request):
    form = loader.get_template("GUI/checkout.html") 
    return HttpResponse(form.render({},request))

def inventory(request):
    form = loader.get_template("GUI/inventory.html") 
    return HttpResponse(form.render({},request))

def queue(request):
    form = loader.get_template("GUI/queue.html") 
    return HttpResponse(form.render({},request))

def history(request):
    form = loader.get_template("GUI/history.html") 
    return HttpResponse(form.render({},request))

def pricebook(request):
    form = loader.get_template("GUI/pricebook.html") 
    return HttpResponse(form.render({},request))