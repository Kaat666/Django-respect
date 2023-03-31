from rest_framework import serializers
from cart.models import Cart


class CartSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = '__all__'


class CartRequestSerializer(serializers.Serializer):
    quantity = serializers.IntegerField()
    price = serializers.IntegerField()
    products = serializers.IntegerField()


class CartResponseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        fields = ['quantity', 'price', 'products']
