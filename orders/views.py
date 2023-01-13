from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.conf import settings

import stripe

from orders.forms import OrderForm
from services.services import TitleMixin

stripe.api_key = settings.STRIPE_SECRET_KEY


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')
    title = 'Оформление заказа'

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)



