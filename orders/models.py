from django.db import models

from users.models import CustomUser
from basket.models import Basket


class Oreders(models.Model):
    CREATED = 0
    PAID = 1
    ON_WAY = 2
    DELIVERED = 3
    STATUSES = (
        (CREATED, 'Создан'),
        (PAID, 'Оплачен'),
        (ON_WAY, 'В пути'),
        (DELIVERED, 'Доставлен'),
    )

    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(max_length=256)
    address = models.CharField(max_length=256)
    basket_history = models.JSONField(default=dict, verbose_name='Корзина заказа')
    created = models.DateTimeField(auto_now_add=True)
    status = models.SmallIntegerField(default=CREATED, choices=STATUSES)
    initiator = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE, verbose_name='Заказчик')

    def __str__(self):
        return f'Заказ {self.id}. {self.first_name} {self.last_name}'

    def update_after_payment(self):
        baskets = Basket.objects.filter(user=self.initiator)
        self.status = self.PAID
        # заполнение basket_history из корзин
        self.basket_history = {
            'purchased_items': [basket.de_json() for basket in baskets], # список купленных продуктов для Stripe
            'total_sum': float(baskets.total_sum()), # итоговая стоимость всех корзин
        }
        baskets.delete() # удаляем корзину оплоченных товаров
        self.save() # сохраняем все изменения

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

