from django.shortcuts import render

from .models import Customer
# Create your views here.

def signup(request):

    return render(request, 'signup.html')