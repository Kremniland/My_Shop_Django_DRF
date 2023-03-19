from django.urls import path
from .views import ProductListView
from basket.views import basket_add, basket_remove

from django.views.decorators.cache import cache_page


app_name = 'prostoapp'

urlpatterns = [
    # path('',   cache_page(30)(ProductListView.as_view()), name='index'),
    path('', ProductListView.as_view(), name='index'),
    path('category/<int:category_id>/', ProductListView.as_view(), name='category'),
    path('page/<int:page>/', ProductListView.as_view(), name='paginator'),

    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]
