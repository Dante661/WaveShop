from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'create_at']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description',
                  'storeId', 'category', 'price', 'create_at',]


class ProductImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImg
        fields = ['id', 'productId', 'imgUrl', ]


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'userId', 'name', 'create_at', ]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'userId', 'quantity']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id', 'cartId', 'productId', 'quantity', 'create_at', ]


class ImgUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgUpload
        fields = ['imgUpload']


class JoinSerializer(serializers.ModelSerializer):
    item_details = ProductSerializer(source='productId')

    class Meta:
        model = CartItem
        fields = ['id', 'cartId', 'itemId',
                  'item_details', 'quantity', 'create_at', ]
