from django.contrib.auth.models import User
from django.db import models
from cart.models import Cart
from order.models import Order


class Users(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name="user", blank=True
    )
    cart = models.ForeignKey(
        Cart, on_delete=models.PROTECT, related_name="cart", blank=True
    )
    order = models.ForeignKey(
        Order, on_delete=models.PROTECT, related_name="order", blank=True
    )
