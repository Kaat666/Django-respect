from rest_framework import serializers
from order.models import Order


class OrderResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['address', 'payment_method', 'products', 'delivery_price']


class OrderRequestSerializer(serializers.Serializer):
    address = serializers.CharField()
    payment_method = serializers.CharField()
    delivery = serializers.CharField()
    x_user = serializers.IntegerField()
    y_user = serializers.IntegerField()


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
