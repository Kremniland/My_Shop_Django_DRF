import stripe
from http import HTTPStatus

from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse, reverse_lazy
from django.conf import settings

from orders.forms import OrderForm
from services.services import TitleMixin
from basket.models import Basket
from orders.models import Oreders

stripe.api_key = settings.STRIPE_SECRET_KEY


class SuccessTemplateView(TitleMixin, TemplateView):
    '''Перенаправит сюда при успешной оплате'''
    template_name = 'orders/success.html'
    title = 'Спасибо за заказ!'


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
        baskets = Basket.objects.filter(user=self.request.user)
        # Берем из документации Stripe https://stripe.com/docs/checkout/quickstart?lang=python
        checkout_session = stripe.checkout.Session.create(
            line_items=baskets.stripe_products(), # вызываем метод у корзины из менеджера BasketQuerySet
            metadata={'order_id': self.object.id},
            mode='payment',
            success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_success')),
            cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('orders:order_canceled')),
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)

    def form_valid(self, form):
        '''Добавляем в форму инициализатора заказа - авторизованный user'''
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)


# @csrf_exempt
# def stripe_webhook_view(request):
#   payload = request.body
#
#   # For now, you only need to print out the webhook payload so you can see
#   # the structure.
#   print(payload)
#
#   return HttpResponse(status=200)

@csrf_exempt
def stripe_webhook_view(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        # Fulfill the purchase...
        fulfill_order(session)

    # Passed signature verification
    return HttpResponse(status=200)

# не переходит в эту ф-ию!!!!!!!!!!!!!!!!!
def fulfill_order(session):
    order_id = int(session.metadata.order_id)
    order = Oreders.objects.get(id=order_id)
    order.update_after_payment()
