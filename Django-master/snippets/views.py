# Create your views here

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from snippets.models import Category
from snippets.models import Product
from snippets.serializers import ProductSerializer
from snippets.serializers import CategorySerializer
from snippets.models import Cart
from snippets.serializers import CartSerializer
from snippets.models import Order
from snippets.serializers import OrderSerializer


# Product request
@api_view(['GET', 'POST'])
def product_list(request, format=None):

    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Cart request
@api_view(['GET', 'PUT', 'DELETE', 'POST'])
def cart_detail(request, format=None):

    if request.method == 'POST':
        serializer = CartSerializer(data=request.data,)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    try:
        carts = Cart.objects.all()
    except Cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        carts.product_id = request.GET.get('name')
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        carts = Cart.objects.filter(id=5).all()
        serializer = CartSerializer(carts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        carts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Category request
@api_view(['GET', 'POST'])
def category_list(request, format=None):

    if request.method == 'GET':
        products = Category.objects.all()
        serializer = CategorySerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Cart request
@api_view(['GET', 'POST'])
def order_list(request, format=None):

    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        cart = Cart.objects.all()
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cart.delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
