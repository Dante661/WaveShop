from django.db import models

# Create your models here.


class User (models.Model):
    """User model"""
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    createDate = models.DateTimeField(auto_now_add=True)


class Store(models.Model):
    """Store"""
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    createDate = models.DateTimeField(auto_now_add=True)


class Item(models.Model):
    """Product"""
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    storeId = models.ForeignKey(Store, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    price = models.IntegerField()
    createDate = models.DateTimeField(auto_now_add=True)


class ItemImg(models.Model):
    """Image"""
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE)
    imgUrl = models.IntegerField()


def upload_location(instance, filename):
    ext = filename.split(".")[-1]
    return "%s/%s.%s" % ("img", datetime.now(), ext)


class ImgUpload(models.Model):
    """Upload Image"""
    imgUpload = models.ImageField(upload_to=upload_location)
# не сделал нормально, почитать про загрузку def upload_location


class Cart(models.Model):
    """Cart quantity"""
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()


class CartItem(models.Model):
    """Cart item model"""
    cartId = models.ForeignKey(Cart, on_delete=models.CASCADE)
    itemId = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    createDate = models.DateTimeField(auto_now_add=True)
