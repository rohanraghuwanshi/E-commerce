from django.urls import path
from .views import store, cart, checkout


urlpatterns = [
    path('', store, name='home'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
]
