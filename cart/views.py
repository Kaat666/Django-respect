from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from cart.models import Cart
from cart.serializers import CartSerializer
from rest_framework.views import APIView


class CartList(APIView):
    @swagger_auto_schema(
        operation_summary="Добавление продукта в корзину",
        responses={
            201: CartSerializer(many=True),
            400: "Не правильный ввод данных",
            500: "Серверная ошибка",
        },
        manual_parameters=[
            openapi.Parameter(
                name="name",
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
        operation_summary="Получение списка всех товаров в корзине",
        responses={200: CartSerializer(many=True), 500: "Серверная ошибка"},
        manual_parameters=[
            openapi.Parameter(
                name="name",
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
        operation_summary="Удаление всех товаров в корзине",
        responses={204: CartSerializer(many=True), 500: "Серверная ошибка"},
        manual_parameters=[
            openapi.Parameter(
                name="name",
                in_=openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def delete(self, request, format=None):
        carts = Cart.objects.all()
        carts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CartDetail(APIView):

    @swagger_auto_schema(
        operation_summary="Получение информации о конкретном товаре",
        responses={200: CartSerializer(many=True), 500: "Серверная ошибка"},
        manual_parameters=[
            openapi.Parameter(
                name="name",
                in_=openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def get(self, request, pk, format=None):
        carts = Cart.objects.filter(pk=pk).first()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Изменение конкретного товара в корзине",
        responses={
            200: CartSerializer(many=True),
            400: "Не правильный ввод данных",
            500: "Серверная ошибка",
        },
        manual_parameters=[
            openapi.Parameter(
                name="name",
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
        operation_summary="Удаление конкретного продукта в корзине",
        responses={204: CartSerializer(many=True), 500: "Серверная ошибка"},
        manual_parameters=[
            openapi.Parameter(
                name="name",
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
