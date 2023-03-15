from django.db import models
from product.models import Product


class Order(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="product", blank=True
    )
    address = models.TextField(max_length=100)
    payment_method = models.TextField(max_length=100)
