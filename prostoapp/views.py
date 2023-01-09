from django.shortcuts import render

from .models import Product, ProductCategory


def index(request):
    context = {}
    return render(request, 'prostoapp/index.html', context)


def products(request):
    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'prostoapp/products.html', context)

