from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import TemplateView, ListView

from .models import Product, ProductCategory
from services.services import TitleMixin

class IndexView(TitleMixin, TemplateView):
    template_name = 'prostoapp/index.html'
    title = 'Главная страница'


# def index(request):
#     context = {'title': 'Главная страница'}
#     return render(request, 'prostoapp/index.html', context)


class ProductListView(TitleMixin, ListView):
    model = Product
    template_name = 'prostoapp/products.html'
    paginate_by = 3
    title = 'Каталог товаров'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.all()
        return context

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        # Если category_id есть в запросе выведет по категории иначе весь список
        return queryset.filter(category_id=category_id) if category_id else queryset

# def products(request, category_id=None, page_number=1):
#     # if category_id:
#     #     products = Product.objects.filter(category_id=category_id)
#     # else:
#     #     products = Product.objects.all()
#     # ==
#     products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
#     per_page = 3
#     paginator = Paginator(products, per_page)
#     products_paginator = paginator.page(page_number)
#     context = {
#         'products': products_paginator,
#         'categories': ProductCategory.objects.all(),
#     }
#     return render(request, 'prostoapp/products.html', context)

