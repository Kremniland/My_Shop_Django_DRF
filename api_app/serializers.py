from rest_framework import serializers

from users.models import CustomUser
from basket.models import Basket
from prostoapp.models import Product, ProductCategory


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=128)
    description = serializers.CharField()


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'price', 'category',)


# class BasketSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Basket
#         fields = ('id', 'user', 'de_json')


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_verified_email', 'image', 'basket')

