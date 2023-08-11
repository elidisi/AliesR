from django.http import HttpResponse
from django.template import loader
from .models import *
from django.http import JsonResponse
from .utils import *
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import datetime
from .utils import create_new_ref_number
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from django.db.models import F


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
        "sisig":Sisig.objects.all(),
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
        current.category = id
        current.itemcount = 1
        current.save()
            
        JsonResponse({'status': 'success'})

        
    form = loader.get_template("GUI/order.html") 
    return HttpResponse(form.render(context,request))

def delete_all(request):
    print("hi")
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

@require_POST
def stocks_update(request):
     # Get the current value of the current variable
    current = CurrentTransaction.objects.all()  # Replace this with your code to get the current value
    # Convert the current value to a list of dictionaries

    for obj in current:
        match obj.category:
            case 'breakfast':
                items = Breakfast.objects.filter(name=obj.items)
                for item in items:
                    print(obj.items)
                    print(item)
                    item.stock = F('stock') - 1
                    item.save()
            case 'noodles':
                items = Noodle.objects.filter(item=obj.items)
                for item in items:
                    item.stock = 0
                    item.save()
            case 'yangchow':
                items = Yangchow.objects.filter(item=obj.items)
                for item in items:
                    item.stock = 0
                    item.save()
            case 'wings':
                items = Wing.objects.filter(item=obj.items)
                for item in items:
                    item.stock = 0
                    item.save()
            case 'sisig':
                items = Sisig.objects.filter(item=obj.items)
                for item in items:
                    item.stock = 0
                    item.save()
            case 'pork':
                items = Pork.objects.filter(item=obj.items)
                for item in items:
                    item.stock = 0
                    item.save()
            case 'chicken':
                items = Chicken.objects.filter(item=obj.items)
                for item in items:
                    item.stock = 0
                    item.save()
            case 'beef':
                items = Beef.objects.filter(item=obj.items)
                for item in items:
                    item.stock = 0
                    item.save()
            case 'seafood':
                items = Seafood.objects.filter(item=obj.items)
                for item in items:
                    item.stock = 0
                    item.save()
            case 'vegatable':
                items = Vegetable.objects.filter(item=obj.items)
                for item in items:
                    item.stock = 0
                    item.save()
            case 'addons':
                items = Addon.objects.filter(item=obj.items)
                for item in items:
                    item.stock = 0
                    item.save()
            case 'drinks':
                items = Drink.objects.filter(item=obj.items)
                for item in items:
                    item.stock = 0
                    item.save()
            case 'snacks':
                items = Snack.objects.filter(item=obj.items)
                for item in items:
                    item.stock = 0
                    item.save()
                    
            case _:
                return redirect('dashboard')
                
    # Return the current value as a JSON response
    return redirect('dashboard')

def checkout(request):
    
    if request.method == 'POST':
        # Retrieve the data from the POST request
        id = request.POST.get('compiled')
        receipt_text = ''
        total = 0
        for item in CurrentTransaction.objects.all():
            receipt_text += f'{item.items} - {item.price}\n'
            total = total + item.price
        receipt_text += f'total = {total}'

        # Update your model or perform other actions here
        current = Receipt(items=receipt_text)
        current.date = datetime.datetime.now()
        current.ref_num = create_new_ref_number()
        current.save()

        JsonResponse({'status': 'success'})
    form = loader.get_template("GUI/checkout.html") 
    return HttpResponse(form.render({},request))

def get_receipt_details(request, receipt_id):
    # Get the Receipt object with the given ID
    receipt = Receipt.objects.get(ref_num=receipt_id)

    # Convert the Receipt object to a dictionary
    receipt_data = {
        'ref_num': receipt.ref_num,
        'date': receipt.date,
        'items': receipt.items,
    }

    # Return the receipt data as a JSON response
    return JsonResponse(receipt_data)


def inventory(request):
    form = loader.get_template("GUI/inventory.html") 
    return HttpResponse(form.render({},request))

@require_POST
def remove_from_cart(request):
    # Get the item id from the request
    item_id = request.POST.get('item_id')

    # Get the cart item with the specified id
    cart_item = CurrentTransaction.objects.filter(items=item_id).first()

    # If the cart item exists, delete it
    if cart_item:
        cart_item.delete()

    # Redirect back to the page that sent the request
    return redirect('order')

def queue(request):
    context = {
        "receipts":Receipt.objects.filter(status='In Queue')
    }
   
    form = loader.get_template("GUI/queue.html") 
    return HttpResponse(form.render(context,request))

def update_receipt_status(request, receipt_id):
    # Get the Receipt object with the given ID
    receipt = Receipt.objects.get(ref_num=receipt_id)

    # Update the status of the receipt to 'Done'
    receipt.status = 'Done'
    receipt.save()

    # Redirect back to the order queue page
    return redirect('queue')

def history(request):
    context = {
    "receipts":Receipt.objects.all(),
   
    }
    
    form = loader.get_template("GUI/history.html") 
    return HttpResponse(form.render(context,request))

def pricebook(request):
    form = loader.get_template("GUI/pricebook.html") 
    return HttpResponse(form.render({},request))