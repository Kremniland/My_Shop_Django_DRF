from django.shortcuts import render

from .models import Product

def get_index(request):
    products = Product.objects.all()
    print(products)
    return render(request, 'prostoapp/index.html', {'products': products})

