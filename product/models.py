from django.db import models
from category.models import Category


class Product(models.Model):
    name = models.TextField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="products"
    )
    description = models.TextField(max_length=250, blank=True)
    price = models.IntegerField()
