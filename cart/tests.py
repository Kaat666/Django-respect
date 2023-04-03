import requests
from django.urls import reverse
from requests.auth import HTTPBasicAuth
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from cart.models import Cart
from cart.serializers import CartResponseSerializer
from cart.views import CartView
from category.models import Category
from order.models import Order
from order.serializers import OrderResponseSerializer
from order.service import delivery_factory
from django.contrib.auth.models import User

from product.models import Product


class CartCreateTest(APITestCase):
    def setUp(self):
        category = Category.objects.create(name="Обувь")
        category.save()
        product = Product.objects.create(name="Черные кроссовки",
                                         price=1000,
                                         category=category,
                                         )
        product.save()

    def tearDown(self):
        Category.objects.all().delete()
        Product.objects.all().delete()
        User.objects.all().delete()
        Cart.objects.all().delete()

    def test_create_cart(self):
        user = User.objects.create(password=123123,
                                   username="test12",
                                   is_superuser=True
                                   )
        user.save()
        resp = requests.post('http://127.0.0.1:8000/cart/',
                             data={
                                 "quantity": 10,
                                 "price": 1000,
                                 "products": 2
                             }, auth=HTTPBasicAuth("test12", 123123))
        data = resp.json()
        response = Cart.objects.filter().first()
        self.assertEqual(response, {
            ("quantity", 10), ("products", 1), ("user_id", 1)
        })
