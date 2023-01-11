from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus

from users.models import CustomUser


class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.path = reverse('users:registration')

    def test_user_registration_get(self):
        '''проверка на гет запрос'''
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Регистрация')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_post_succes(self):
        '''проверка пост запрос на регистрацию'''
        data = { # создаемdata для заполнения формы регистрации
            'first_name': 'user1', 'last_name': 'user1',
            'username': 'user1', 'email': 'user1@mail.ru',
            'password1': '1234', 'password2': '1234',
        }
        username = data['username']
        self.assertFalse(CustomUser.objects.filter(username=username).exists()) # проверяем отсутствие пользователя до нашего запроса

        response = self.client.post(self.path, data) # отправляем данные на регистрацию

        self.assertEqual(response.status_code, HTTPStatus.FOUND) # статус редиректа послерегистрации
        self.assertRedirects(response, reverse('users:login')) # проверяем куда редирект
        self.assertTrue(CustomUser.objects.filter(username=username).exists()) # был ли создан пользователь с таким username








