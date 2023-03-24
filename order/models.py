from django.db import models
from product.models import Product
from user.models import User


class Order(models.Model):
    products = models.ManyToManyField(
        Product, related_name="orders", blank=True
    )
    address = models.TextField(max_length=100)
    payment_method = models.TextField(max_length=100)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="userss",
    )
