from django.db import models
from product.models import Product


class Cart(models.Model):
    products = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="products", blank=True
    )
    quantity = models.IntegerField()
    price = models.IntegerField(default=0)
