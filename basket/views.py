from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from prostoapp.models import Product
from .models import Basket


@login_required # не авторизованного user перенаправит на LOGIN_URL
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    # Возвращаем туда где находился пользователь
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required # не авторизованного user перенаправит на LOGIN_URL
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

