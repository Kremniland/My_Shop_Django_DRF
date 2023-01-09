from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Product, ProductCategory


def index(request):
    context = {}
    return render(request, 'prostoapp/index.html', context)


def products(request, category_id=None, page_number=1):
    # if category_id:
    #     products = Product.objects.filter(category_id=category_id)
    # else:
    #     products = Product.objects.all()
    # ==
    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    per_page = 3
    paginator = Paginator(products, per_page)
    products_paginator = paginator.page(page_number)
    context = {
        'products': products_paginator,
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'prostoapp/products.html', context)

