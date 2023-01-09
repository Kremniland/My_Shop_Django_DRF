from django.contrib import admin

from .models import Basket


class BasketAdmin(admin.TabularInline): # При связи ForeigenKey применим как inline к User
    model = Basket
    fields = ['product', 'quantity']
    extra = 0 # Не выводить полей для заполнения


