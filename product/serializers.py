from rest_framework import serializers
from product.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"


class ProductResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['name', 'category', 'price']
