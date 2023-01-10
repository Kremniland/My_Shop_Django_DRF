from django.contrib import admin

from .models import CustomUser, EmailVerification
from basket.admin import BasketAdmin


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'is_verified_email']
    inlines = [BasketAdmin]


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ['code', 'user', 'expiration', 'create']
    fields = ['code', 'user', 'expiration', 'create']
    readonly_fields = ['create']

