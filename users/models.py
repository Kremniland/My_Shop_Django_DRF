from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='user_images', null=True, blank=True)

    class Meta:
        db_table = 'CustomUser'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'




