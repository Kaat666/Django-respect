from django.db import models


# Product category model
class Category(models.Model):
    name = models.TextField(max_length=100)


# Specific Product Model
class Product(models.Model):
    name = models.TextField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name="products"
    )
    description = models.TextField(max_length=250, blank=True)
    price = models.IntegerField()


# Cart model
class Cart(models.Model):
    products = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="products", blank=True
    )
    quantity = models.IntegerField()
    price = models.IntegerField(default=0)


# Order model
class Order(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.PROTECT, related_name="product", blank=True
    )
    address = models.TextField(max_length=100)
    payment_method = models.TextField(max_length=100)


class Meta:
    ordering = ["created"]