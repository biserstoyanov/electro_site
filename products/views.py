from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product

def products_list(request):
    products = Product.objects.all()
    return render(request, "products/products.html", {
        "products": products
    })