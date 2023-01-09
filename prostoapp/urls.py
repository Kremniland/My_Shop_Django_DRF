from django.urls import path
from .views import index, products
from basket.views import basket_add, basket_remove


app_name = 'prostoapp'

urlpatterns = [
    # path('', index, name='home'),
    path('', products, name='index'),
    path('category/<int:category_id>/', products, name='category'),
    path('page/<int:page_number>/', products, name='paginator'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
