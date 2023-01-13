import stripe
from http import HTTPStatus

from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse, reverse_lazy
from django.conf import settings

from orders.forms import OrderForm
from services.services import TitleMixin

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessTemplateView(TitleMixin, TemplateView):
    '''Перенаправит сюда при успешной оплате'''
    template_name = 'orders/success.html'
    title = 'Store - Спасибо за заказ!'


class CanceledTemplateView(TemplateView):
    '''Перенаправит сюда если оплата не прошла'''
    template_name = 'orders/cancled.html'


class OrderCreateView(TitleMixin, CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')
    title = 'Оформление заказа'

    def post(self, request, *args, **kwargs):
        '''Для оплаты Stripe'''
        super(OrderCreateView, self).post(request, *args, **kwargs)
        # Берем из документации Stripe https://stripe.com/docs/checkout/quickstart?lang=python
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': 'price_1MPnbiKgOEROgSZruQC5DDk1', # Регистрируем в БД Stripr один продукт для теста
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_success')),
            cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_canceled')),
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        '''Добавляем в форму инициализатора заказа - авторизованный user'''
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)



