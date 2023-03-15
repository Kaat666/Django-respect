from rest_framework import serializers
from cart.models import Cart
from product.models import Product


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = "__all__"
