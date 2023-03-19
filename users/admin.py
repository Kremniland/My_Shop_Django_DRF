from django.contrib import admin

from .models import CustomUser, EmailVerification
from basket.admin import BasketAdmin


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['pk', 'username', 'is_verified_email']
    list_display_links = ('username',)
    inlines = [BasketAdmin]


@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ['code', 'user', 'expiration', 'create']
    fields = ['code', 'user', 'expiration', 'create']
    readonly_fields = ['create']

