from django.forms import model_to_dict
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from users.models import CustomUser
from basket.models import Basket
from prostoapp.models import Product, ProductCategory
from api_app.serializers import CustomUserSerializer, CategorySerializer


class CategoryAPIView(APIView):
    '''работа с катенгориями товара'''
    def get(self, request):
        '''вывод списка категорий'''
        categories = ProductCategory.objects.all()
        return Response({'categories': CategorySerializer(categories, many=True).data})


class BasketsUserAPIView(APIView):
    '''работа с корзинами пользователя без сериалайзера'''
    def get(self, request):
        '''отдает данные метода basket de_json() авторизованного пользователя'''
        baskets = Basket.objects.filter(user=1).select_related('product')
        lst_basket = []
        for basket in baskets:
            lst_basket.append(basket.de_json())
        return Response({'baskets': lst_basket})


class UserViewSet(ModelViewSet):
    '''получение списка User, добавление, редактирование и удаление для администратора'''
    queryset = CustomUser.objects.all().order_by('id').prefetch_related('basket')
    serializer_class = CustomUserSerializer
    permission_classes = (IsAdminUser,)



