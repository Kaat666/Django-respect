from rest_framework import serializers
from order.models import Order, Pvz


class OrderResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['address', 'payment_method', 'products', 'price']


class OrderRequestSerializer(serializers.Serializer):
    address = serializers.CharField()
    payment_method = serializers.CharField()
    delivery = serializers.CharField()


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class PvzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pvz
        fields = '__all__'
