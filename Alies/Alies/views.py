from django.http import HttpResponse
from django.template import loader
from .models import *
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from .utils import *
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count, F, Value





def dashboard(request):
    context = {
        'breakfast': Breakfast.objects.all()
    }
    
    form = loader.get_template("GUI/dashboard.html") 
    return HttpResponse(form.render(context,request))

def login(request):
    form = loader.get_template("GUI/login.html")
    return HttpResponse(form.render({},request))


@csrf_exempt
def order(request):
    context = {
        "breakfast":Breakfast.objects.all(),
        "noodles":Noodle.objects.all(),
        "yangchow":Yangchow.objects.all(),
        "wings":Wing.objects.all(),
        "pork":Pork.objects.all(),
        "chicken":Chicken.objects.all(),
        "beef":Beef.objects.all(),
        "seafood":Seafood.objects.all(),
        "vegatable":Vegetable.objects.all(),
        "addons":Addon.objects.all(),
        "drinks":Drink.objects.all(),
        "snacks":Snack.objects.all(),
        "current":CurrentTransaction.objects.all(),
    }
    
    if request.method == 'POST':
        # Retrieve the data from the POST request
        id = request.POST.get('id')
        name = request.POST.get('name')
        price = request.POST.get('price')

        # Update your model or perform other actions here
        current = CurrentTransaction()
        current.items = name
        current.price = price
        current.itemcount = 1
        current.save()

        JsonResponse({'status': 'success'})

        
    form = loader.get_template("GUI/order.html") 
    return HttpResponse(form.render(context,request))

@csrf_exempt
def delete_all(request):
    if request.method == 'POST':
        # Delete all objects of MyModel
        CurrentTransaction.objects.all().delete()

        # Return a JSON response
        form = loader.get_template("GUI/order.html") 
        return JsonResponse({'status': 'success'})
    
    # Handle other request methods here

def get_current(request):
     # Get the current value of the current variable
    current = CurrentTransaction.objects.all()  # Replace this with your code to get the current value

    # Convert the current value to a list of dictionaries
    current_list = []
    for obj in current:
        current_list.append({
            'items': obj.items,
            'price': obj.price,
        })

    # Return the current value as a JSON response
    return JsonResponse(current_list, safe=False)

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