from django.db import models
from order.service import DeliveryType
from product.models import Product
from django.contrib.auth.models import User


class Order(models.Model):
    products = models.ManyToManyField(
        Product, related_name="orders", blank=True
    )
    address = models.TextField(max_length=100)
    payment_method = models.TextField(max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="userss",
    )
    price = models.IntegerField()


class Pvz(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    type = models.TextField(null=False)
