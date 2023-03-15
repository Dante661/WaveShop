from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email', 'createDate']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'description',
                  'storeId', 'category', 'price', 'createDate',]


class ItemImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImg
        fields = ['id', 'title', 'itemId', 'imgUrl', ]


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'userId', 'name', 'createDate', ]


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImg
        fields = ['id', 'userId', 'quantity']


class CartItemImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemImg
        fields = ['id', 'cartId', 'itemId', 'quantity', 'createDate', ]


class ImgUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImgUpload
        fields = ['imgUpload']


class JoinSerializer(serializers.ModelSerializer):
    item_details = ItemSerializer(source='itemId')

    class Meta:
        model = CartItem
        fields = ['id', 'cartId', 'itemId',
                  'item_details', 'quantity', 'createDate', ]
