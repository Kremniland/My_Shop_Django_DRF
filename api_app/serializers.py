from rest_framework import serializers

from users.models import CustomUser
from basket.models import Basket
from prostoapp.models import Product, ProductCategory


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductCategory
        fields = ('id', 'name', 'description',)


class ProductSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(source='category')

    class Meta:
        model = Product
        fields = ('name', 'price','quantity', 'category_name',)


# class BasketSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Basket
#         fields = ('id', 'user', 'de_json')


class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'is_verified_email', 'image',)

