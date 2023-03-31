from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from cart.models import Cart
from cart.serializers import CartSerializer, CartRequestSerializer, CartResponseSerializer
from rest_framework.views import APIView

from product.models import Product


class CartView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_summary="Добавление продукта в корзину",
        responses={
            201: CartSerializer,
            400: "Не правильный ввод данных",
            500: "Серверная ошибка",
        },
        request_body=CartRequestSerializer
    )
    def post(self, request):
        cart = Cart(
            products=Product.objects.filter(pk=request.data.get("products")).first(),
            quantity=request.data.get("quantity"),
            price=request.data.get("price"),
            user_id=request.user.id
        )
        cart.save()
        serializer = CartResponseSerializer(cart)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary="Получение списка всех товаров в корзине",
        responses={200: CartSerializer(many=True), 500: "Серверная ошибка"},
    )
    def get(self, request):
        cart = Cart.objects.filter(user_id=request.user.id).all()
        serializer = CartResponseSerializer(cart, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Удаление всех товаров в корзине",
        responses={204: CartSerializer, 500: "Серверная ошибка"},
    )
    def delete(self, request):
        cart = Cart.objects.filter(user_id=request.user.id).all()
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartDetail(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_summary="Получение информации о конкретном товаре",
        responses={200: CartSerializer, 500: "Серверная ошибка"},
    )
    def get(self, request, pk):
        carts = Cart.objects.filter(pk=pk, user_id=request.user.id).first()
        serializer = CartResponseSerializer(carts)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Изменение конкретного товара в корзине",
        responses={
            200: CartSerializer(many=True),
            400: "Не правильный ввод данных",
            500: "Серверная ошибка",
        },
        request_body=CartRequestSerializer
    )
    def put(self, request, pk):
        product = Cart.objects.filter(pk=pk, user_id=request.user.id).first()
        serializer = CartResponseSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Удаление конкретного продукта в корзине",
        responses={204: CartSerializer(many=True), 500: "Серверная ошибка"},
    )
    def delete(self, request, pk):
        carts = Cart.objects.filter(pk=pk, user_id=request.user.id).first()
        carts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
