from django.shortcuts import render
from django.http import JsonResponse

import json, datetime

from .models import *
from .utils import cookieCart, cartData, guestOrder

# Create your views here.


def store(request):

    data = cartData(request)

    products = Product.objects.all()

    context = {
        "products": products,
        "cartItems": data["cartItems"],
    }

    return render(request, "store/store.html", context)


def cart(request):

    data = cartData(request)

    context = {
        "items": data["items"],
        "order": data["order"],
        "cartItems": data["cartItems"],
    }

    return render(request, "store/cart.html", context)


def checkout(request):

    data = cartData(request)

    context = {
        "items": data["items"],
        "order": data["order"],
        "cartItems": data["cartItems"],
    }

    return render(request, "store/checkout.html", context)


def update_item(request):
    data = json.loads(request.body)
    productID = data["productID"]
    action = data["action"]

    customer = request.user.customer
    product = Product.objects.get(id=productID)

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderitem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderitem.quantity = orderitem.quantity + 1
    elif action == "remove":
        orderitem.quantity = orderitem.quantity - 1

    orderitem.save()

    if orderitem.quantity <= 0:
        orderitem.delete()

    return JsonResponse("Item was added", safe=False)


def process_order(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

    else:
        customer, order = guestOrder(request, data)

    total = float(data["form"]["total"])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data["shipping"]["address"],
            city=data["shipping"]["city"],
            state=data["shipping"]["state"],
            zipcode=data["shipping"]["zipcode"],
        )

    return JsonResponse("Data Recieved", safe=False)
