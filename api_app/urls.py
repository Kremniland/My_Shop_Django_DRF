from django.urls import path, include

from rest_framework import routers

from api_app.views import UserViewSet, BasketsUserAPIView, CategoryViewSet, ProductViewSet

app_name = 'api_app'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'products', ProductViewSet, basename='products')


urlpatterns = [
    path('baskets_user/', BasketsUserAPIView.as_view(), name='baskets_user'),
    # path('auth/drf/', include('rest_framework.urls')), # подключение drf urls, для регистрации по сессиям
]

urlpatterns += router.urls