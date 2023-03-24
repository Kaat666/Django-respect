from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from cart.models import Cart
from order.models import Order
from order.serializers import OrderSerializer
from rest_framework.views import APIView


class OrderView(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_summary="Получение списка всех заказов",
        responses={200: OrderSerializer(many=True), 500: "Серверная ошибка"},
    )
    def get(self, request):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Оформление заказа",
        responses={
            201: OrderSerializer,
            400: "Не правильный ввод данных",
            500: "Серверная ошибка",
        },
        request_body=OrderSerializer
    )
    def post(self, request):
        cart = Cart.objects.filter(user_id=request.user.id).all()
        if cart is None:
            return Response(status=status.HTTP_404_NOT_FOUND)
        order = Order(address=request.data.get("address"),
                      payment_method=request.data.get("payment_method"),
                      user_id=request.user.id
                      )
        order.save()
        for item in cart:
            order.products.add(item.products)
        order.save()
        cart.delete()
        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderDetail(APIView):
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_summary="Получение информации о конкретном заказе",
        responses={200: OrderSerializer, 500: "Серверная ошибка"},
    )
    def get(self, request, pk):
        orders = Order.objects.filter(pk=pk).first()
        serializer = OrderSerializer(orders)
        return Response(serializer.data)
