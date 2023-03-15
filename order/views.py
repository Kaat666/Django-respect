from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from cart.models import Cart
from order.models import Order
from order.serializers import OrderSerializer
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class OrderList(APIView):
    @swagger_auto_schema(
        operation_summary="Получение списка всех заказов",
        responses={200: OrderSerializer(many=True), 500: "Серверная ошибка"},
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
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Оформление заказа",
        responses={
            201: OrderSerializer(many=True),
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
    def post(self, request, products_id, format=None):
        cart = Cart.objects.all()
        serializer = OrderSerializer(cart, many=True)
        if serializer.is_valid():
            serializer.save()
            cart.delete()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetail(APIView):
    @swagger_auto_schema(
        operation_summary="Получение информации о конкретном заказе",
        responses={200: OrderSerializer(many=True), 500: "Серверная ошибка"},
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
        orders = Order.objects.filter(pk=pk).first()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
