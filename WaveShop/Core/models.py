from datetime import datetime

from django.db import models


# Create your models here.


class User(models.Model):
    """Модель пользователя"""

    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    create_at = models.DateTimeField(auto_now_add=True)


class Store(models.Model):
    """Модель магазина"""

    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    """Модель продуктов"""

    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    storeId = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)


class ProductImg(models.Model):
    """Изображение продукта"""

    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    imgUrl = models.IntegerField()


def upload_location(instance, filename):
    ext = filename.split(".")[-1]
    return "%s/%s.%s" % ("img", datetime.now(), ext)


class ImgUpload(models.Model):
    """Загрузка изо"""

    imgUpload = models.ImageField(upload_to=upload_location)


# не сделал нормально, почитать про загрузку def upload_location


class Cart(models.Model):
    """Cart quantity корзина"""

    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class CartItem(models.Model):
    """Cart item model Модель корзины, ее итемы"""

    cartId = models.ForeignKey(Cart, on_delete=models.CASCADE)
    itemId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    create_at = models.DateTimeField(auto_now_add=True)


class Promo(models.Model):
    """Промокоды надо подумать как подвязывать"""

    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)


class Storage(models.Model):
    """Склады
    адресс и наличие продуктов через продукт ид
    """

    adress = models.CharField(max_length=400)
    productId = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()


# class Stock(models.Model):
#     """ПВЗ"""

#     pass
