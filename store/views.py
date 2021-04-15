from django.shortcuts import render
from django.http import JsonResponse

import json

from .models import *

# Create your views here.



def store(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order = {
            'get_cart_total':0,
            'get_cart_items':0,
            'shipping':False,
        }
        cartItems =order['get_cart_items']

    products = Product.objects.all()

    context = {
        'products': products,
        'cartItems': cartItems,
    }

    return render(request, "store/store.html", context)


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order = {
            'get_cart_total':0,
            'get_cart_items':0,
            'shipping':False,
        }
        cartItems = order['get_cart_items']

    context = {
        'items':items,
        'order':order,
        'cartItems': cartItems,
    }

    return render(request, "store/cart.html", context)


def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items=[]
        order = {
            'get_cart_total':0,
            'get_cart_items':0,
            'shipping':False,
        }
        cartItems = order['get_cart_items']

    context = {
        'items':items,
        'order':order,
        'cartItems': cartItems,
    }

    return render(request, "store/checkout.html", context)


def update_item(request):
    data = json.loads(request.body)
    productID = data['productID']
    action = data['action']

    customer = request.user.customer
    product = Product.objects.get(id=productID)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action =='add':
        orderitem.quantity = (orderitem.quantity + 1)
    elif action=='remove':
        orderitem.quantity = (orderitem.quantity - 1)

    orderitem.save()

    if orderitem.quantity <=0:
        orderitem.delete()

    return JsonResponse('Item was added', safe=False)


def process_order(request):
    return JsonResponse('Data Recieved', safe=False)