from django.contrib import admin

from .models import CustomUser
from basket.admin import BasketAdmin


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username']
    inlines = [BasketAdmin]
