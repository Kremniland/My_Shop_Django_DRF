from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf.urls.static import static
from django.conf import settings

from prostoapp.views import IndexView
from orders.views import stripe_webhook_view


schema_view = get_schema_view(
    openapi.Info(
        title="Shop API",
        default_version='v1',
        description="Docs",
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="contact@snippets.local"),
        # license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger(?P<format>\.json|\.yaml)', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

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



