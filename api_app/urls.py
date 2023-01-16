from django.urls import path

from rest_framework import routers

from api_app.views import UserViewSet, BasketsUserAPIView, CategoryAPIView

app_name = 'api_app'

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('baskets_user/', BasketsUserAPIView.as_view(), name='baskets_user'),
    path('categories/', CategoryAPIView.as_view(), name='categories'),
]

urlpatterns += router.urls