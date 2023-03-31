from django.db import models
from product.models import Product
from django.contrib.auth.models import User


class Cart(models.Model):
    products = models.ForeignKey(
        Product, related_name="carts", blank=True, on_delete=models.CASCADE,
    )
    quantity = models.IntegerField()
    price = models.IntegerField(default=0)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="users", blank=True
    )
