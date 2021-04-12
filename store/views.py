from django.shortcuts import render

from .models import Product, Category

# Create your views here.


def index(request):

    categories = Category.get_all_categories()

    categoryId = request.GET['category']

    if categoryId:
        products = Product.get_all_products_by_id(categoryId)
    else:
        products = Product.get_all_products()
    

    context = {
        "products": products,
        "categories": categories,
    }

    return render(request, "index.html", context)