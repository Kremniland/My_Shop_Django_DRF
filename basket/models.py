from django.db import models

from users.models import CustomUser
from prostoapp.models import Product


class BasketQuerySet(models.QuerySet):
    '''создаем менеджер для определения total_sum total_quantity
    общая сумма во всех корзинах и общее кол-во товара во всех корзинах CustomUser'''
    def total_sum(self):
        return sum(basket.sum() for basket in self)

    def total_quantity(self):
        return sum(basket.quantity for basket in self)


class Basket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    create_timestamp = models.DateTimeField(auto_now_add=True)
    # Преопределяем objects и теперь у корзин есть методы из BasketQuerySet класса
    objects = BasketQuerySet.as_manager()

    def __str__(self):
        return f'Корзина для {self.user.username}, Продукт {self.product.name}'

    def sum(self):
        return self.product.price * self.quantity

    class Meta:
        db_table = 'Basket'
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

