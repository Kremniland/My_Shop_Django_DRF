from rest_framework import serializers

from users.models import CustomUser
from basket.models import Basket
from prostoapp.models import Product, ProductCategory


class ProductSerializer(serializers.ModelSerializer):
    # выведет метод __str__ в модели категории
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'price','quantity', 'category',)


class CategorySerializer(serializers.ModelSerializer):
    # выведет product поле name, many=True - значит ко многим
    product = serializers.SlugRelatedField(slug_field='name', read_only=True, many=True)

    class Meta:
        model = ProductCategory
        fields = ('id', 'name', 'description', 'product')


class BasketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Basket
        fields = ('id', 'user', 'de_json') # de_json - метод в модели Basket


class CustomUserSerializer(serializers.ModelSerializer):
    # использование метода со вложенным сериалайзером
    basket_user = serializers.SerializerMethodField()

    def get_basket_user(self, obj):
        # obj - объект CustomUser
        baskets = obj.basket.all()
        if not baskets:
            return None
        return BasketSerializer(baskets, many=True).data

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_verified_email', 'image', 'basket_user')
