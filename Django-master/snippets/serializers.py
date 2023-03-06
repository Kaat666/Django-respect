from rest_framework import serializers
from snippets.models import Product
from snippets.models import Cart
from snippets.models import Category
from snippets.models import Order


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True
    )
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    products_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='products',
        write_only=True
    )
    products = ProductSerializer(read_only=True)

    class Meta:
        model = Cart
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    cart_id = serializers.PrimaryKeyRelatedField(
        queryset=Cart.objects.all(),
        source='cart',
        write_only=True
    )
    cart = CartSerializer(read_only=True)

    class Meta:
        model = Order
        fields = '__all__'
