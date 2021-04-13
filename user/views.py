from django.shortcuts import render, redirect

from .models import Customer
# Create your views here.

def signup(request):
    if request.method == "POST":
        customer = Customer(
            first_name = request.POST.get('first_name'),
            last_name = request.POST.get('last_name'),
            email = request.POST.get('email'),
            password = request.POST.get('password')
        )
        customer.save()

    return render(request, 'signup.html')