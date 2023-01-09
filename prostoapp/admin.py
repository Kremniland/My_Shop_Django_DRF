from django.contrib import admin

from .models import ProductCategory, Product


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'quantity', 'category']
    fields = ['name', 'description', 'image', ('price', 'quantity'), 'category']
    # readonly_fields = ['description']
    search_fields = ['name']
    ordering = ['name']
