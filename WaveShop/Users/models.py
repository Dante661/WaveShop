from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to="imageUser")


# Create your models here.
