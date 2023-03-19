from django.core.mail import send_mail
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.utils.timezone import now

from django.conf import settings


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='user_images', null=True, blank=True)
    is_verified_email = models.BooleanField(default=False) # подтвержденли email

    class Meta:
        db_table = 'CustomUser'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class EmailVerification(models.Model):
    '''после регистрации пользователя письмо со ссылкой отправится на почту'''
    code = models.UUIDField(unique=True)
    user = models.ForeignKey(to=CustomUser, on_delete=models.CASCADE)
    create = models.DateTimeField(auto_now_add=True)
    expiration = models.DateTimeField()  # срок годности ссылки

    def __str__(self):
        return f'Верификация для {self.user.email}'

    def send_verification_mail(self):
        '''отправка email со ссылкой для подтверждения verification_link'''
        link = reverse('users:email_verify', kwargs={'email': self.user.email, 'code': self.code})
        verification_link = f'{settings.DOMAIN_NAME}{link}'
        subject = 'Подтверждение учетной записи'
        message = 'Для подтверждения {} пройдите по ссылке: {}'.format(
            self.user.email,
            verification_link
        )
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email],
            fail_silently=False,
        )

    def is_expired(self):
        '''проверка срока годности ссылки'''
        return True if now() >= self.expiration else False


