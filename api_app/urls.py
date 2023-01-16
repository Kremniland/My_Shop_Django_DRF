from django.urls import path

from rest_framework import routers

from api_app.views import UserViewSet, BasketsUserAPIView, CategoryViewSet, ProductViewSet
app_name = 'api_app'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'category', CategoryViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
    path('baskets_user/', BasketsUserAPIView.as_view(), name='baskets_user'),
]

urlpatterns += router.urls