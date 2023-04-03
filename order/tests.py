from unittest import TestCase
import requests
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.test import APITestCase
from cart.models import Cart
from category.models import Category
from order.models import Order
from order.service import delivery_factory
from order.views import OrderView
from django.contrib.auth.models import User
from product.models import Product


class OrderCreateTest(TestCase):
    def setUp(self):
        category = Category.objects.create(name="Обувь")
        product = Product.objects.create(name="Черные кроссовки",
                                         price=1000,
                                         category=category,
                                         )
        user = User.objects.create(password=123123,
                                   username="test1"
                                   )
        Cart.objects.create(quantity=10,
                            price=9000,
                            products=product,
                            user=user
                            )

    def tearDown(self):
        Category.objects.all().delete()
        Product.objects.all().delete()
        User.objects.all().delete()
        Cart.objects.all().delete()
        Order.objects.all().delete()

    def test_create_order(self):
        delivery = 'Yandex'
        service = delivery_factory(delivery)
        delivery_price = service.calc_delivery_price(address="Цирк",
                                                     x_user=1500,
                                                     y_user=4000)
        requests.post('http://127.0.0.1:8000/order/',
                      data={
                          "address": "Цирк",
                          "payment_method": "Картой",
                          "delivery_price": delivery_price,
                          "user_id": 1
                      })
        response = Order.objects.values_list()
        self.assertEqual(response, [
            ("address", "Цирк"), ("payment_method", "Картой"), ("delivery_price", 2000), ("user_id", 1), ("products", [1])
        ])
