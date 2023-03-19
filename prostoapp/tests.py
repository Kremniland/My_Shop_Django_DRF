from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

from prostoapp.models import Product, ProductCategory


class IndexViewTestCase(TestCase):

    def test_view(self): # название должно начинаться с test
        path = reverse('index') # http://127.0.0.1:8000/ возьмется этот адресс
        response = self.client.get(path) # делаемget запрос на путь path

        print(response)

        self.assertEqual(response.status_code, HTTPStatus.OK) # значит статус 200
        self.assertEqual(response.context_data['title'], 'Главная страница') # проверка title 'Главная страница'
        self.assertTemplateUsed(response, 'prostoapp/index.html') # проверка какой шаблон выведет


class ProductsListViewTestCase(TestCase):
    fixtures = ['categorys.json', 'productss.json'] # заполняем БД fixtures не работает utf-8

    def test_list(self):
        path = reverse('prostoapp:index')
        response = self.client.get(path) # делаемget запрос на путь path

        self.assertEqual(response.status_code, HTTPStatus.OK) # значит статус 200
        self.assertEqual(response.context_data['title'], 'Каталог товаров') # проверка title 'Главная страница'
        self.assertTemplateUsed(response, 'prostoapp/products.html') # проверка какой шаблон выведет


