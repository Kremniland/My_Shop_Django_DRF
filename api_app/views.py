from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly,  IsAuthenticated
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action

from users.models import CustomUser
from basket.models import Basket
from prostoapp.models import Product, ProductCategory
from api_app.serializers import CustomUserSerializer, CategorySerializer, ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all().select_related('category')
    serializer_class = ProductSerializer

    @action(methods=['get'], detail=False)
    def categories(self, request):
        '''добавит get запрос к категориям'''
        categories = ProductCategory.objects.all()
        return Response({'category': [category.name for category in categories]})

    def get_permissions(self):
        '''просматривать могут все а редактировать только админ'''
        if self.action == 'list' or self.action=='retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class CategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = CategorySerializer


    def get_permissions(self):
        '''просматривать могут все а редактировать только админ'''
        if self.action == 'list' or self.action=='retrieve':
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class UserViewSet(ModelViewSet):
    '''получение списка User, добавление, редактирование и удаление для администратора'''
    queryset = CustomUser.objects.all().order_by('id')#.prefetch_related('basket')
    serializer_class = CustomUserSerializer
    permission_classes = (IsAdminUser,)


class BasketsUserAPIView(APIView):
    '''работа с корзинами пользователя без сериалайзера'''
    def get(self, request):
        '''отдает данные метода basket de_json() авторизованного пользователя'''
        baskets = Basket.objects.filter(user=request.user).select_related('product')
        lst_basket = []
        for basket in baskets:
            lst_basket.append(basket.de_json())
        return Response({'baskets': lst_basket}) # преобразует словарь в Json


