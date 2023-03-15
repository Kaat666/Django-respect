from rest_framework import serializers
from order.models import Order
from product.models import Product


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
