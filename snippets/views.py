# Create your views here

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from snippets.models import Category
from snippets.models import Product
from snippets.serializers import ProductSerializer
from snippets.serializers import CategorySerializer
from snippets.models import Cart
from snippets.serializers import CartSerializer
from snippets.models import Order
from snippets.serializers import OrderSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


# Product request
class ProductList(APIView):
    @swagger_auto_schema(
        operation_summary='Получение всех продуктов',
        responses={200: ProductSerializer(many=True), 500: 'Серверная ошибка'},
        manual_parameters=[
            openapi.Parameter(
                name='name',
                in_=openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary='Добавление продукта в список',
        responses={201: ProductSerializer(many=True), 404: 'Не правильный ввод данных ', 500: 'Серверная ошибка'},
        manual_parameters=[
            openapi.Parameter(
                name='name',
                in_=openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Cart request
class CartDetail(APIView):
    @swagger_auto_schema(
        operation_summary='Добавление продукта в корзину',
        responses={201: CartSerializer(many=True), 400: 'Не правильный ввод данных', 500: 'Серверная ошибка'},
        manual_parameters=[
            openapi.Parameter(
                name='name',
                in_=openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def post(self, request, format=None):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Получение списка всех товаров в корзине',
        responses={200: CartSerializer(many=True), 500: 'Серверная ошибка'},
        manual_parameters=[
            openapi.Parameter(
                name='name',
                in_=openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def get(self, request, format=None):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary='Изменение конкретного товара в корзине',
        responses={200: CartSerializer(many=True), 400: 'Не правильный ввод данных',500: 'Серверная ошибка'},
        manual_parameters=[
            openapi.Parameter(
                name='name',
                in_=openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def put(self, request, pk, format=None):
        product = Cart.objects.filter(pk=pk).first()
        serializer = CartSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary='Удаление конкретного продукта в корзине',
        responses={204: CartSerializer(many=True), 500: 'Серверная ошибка'},
        manual_parameters=[
            openapi.Parameter(
                name='name',
                in_=openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def delete(self, request, pk, format=None):
        carts = Cart.objects.filter(pk=pk).first()
        carts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Category request
class CategoryDetail(APIView):
    @swagger_auto_schema(
        operation_summary='Получение списка всех существующих категорий',
        responses={200: CategorySerializer(many=True), 500: 'Серверная ошибка'},
        manual_parameters=[
            openapi.Parameter(
                name='name',
                in_=openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def get(self, request, format=None):
        products = Category.objects.all()
        serializer = CategorySerializer(products, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary='Добавление новой категории',
        responses={201: CategorySerializer(many=True), 400: 'Не правильный ввод данных', 500: 'Серверная ошибка'},
        manual_parameters=[
            openapi.Parameter(
                name='name',
                in_=openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Cart request
class OrderList(APIView):
    @swagger_auto_schema(
        operation_summary='Получение списка всех заказов',
        responses={200: OrderSerializer(many=True), 500: 'Серверная ошибка'},
        manual_parameters=[
            openapi.Parameter(
                name='name',
                in_=openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary='Получение всех продуктов',
        responses={201: OrderSerializer(many=True), 400: 'Не правильный ввод данных', 500: 'Серверная ошибка'},
        manual_parameters=[
            openapi.Parameter(
                name='name',
                in_=openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def post(self, request, products_id, format=None):
        cart = get_object_or_404(Cart, products_id=products_id)
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cart.delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriesProduct(APIView):
    @swagger_auto_schema(
        operation_summary='Получение всех товаров находящихся в определенной категории',
        responses={200: ProductSerializer(many=True), 500: 'Серверная ошибка'},
        manual_parameters=[
            openapi.Parameter(
                name='name',
                in_=openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def get(self, request, category_id, format=None):
        products = Product.objects.filter(category_id=category_id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
