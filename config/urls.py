from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings # Правильный импорт settings подтянет все настройки

from prostoapp.views import IndexView
from orders.views import stripe_webhook_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),

    path('products/', include('prostoapp.urls', namespace='prostoapp')),
    path('users/', include('users.urls', namespace='users')),

    path('accounts/', include('allauth.urls')),
    path('orders/', include('orders.urls', namespace='orders')),

    path('webhook/stripe/', stripe_webhook_view, name='stripe_webhook'),
]

if settings.DEBUG == True:
    urlpatterns.append(path('__debug__/', include('debug_toolbar.urls')))
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



