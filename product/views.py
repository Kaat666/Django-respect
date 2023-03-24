from django.http import Http404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.views import APIView


class ProductView(APIView):
    permission_classes = ()

    @swagger_auto_schema(
        operation_summary="Получение всех продуктов",
        responses={200: ProductSerializer(many=True), 500: "Серверная ошибка"},
    )
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Добавление продукта в список",
        responses={
            201: ProductSerializer(many=True),
            404: "Не правильный ввод данных ",
            500: "Серверная ошибка",
        },
        request_body=ProductSerializer
    )
    def post(self, request):
        if request.user.is_superuser:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                products = Product.objects.all()
                serializer = ProductSerializer(products, many=True)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise Http404


class ProductDetail(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @swagger_auto_schema(
        operation_summary="Получение информации о конретном продукте",
        responses={200: ProductSerializer(many=True), 500: "Серверная ошибка"},
    )
    def get(self, request, pk):
        products = Product.objects.filter(pk=pk).first()
        serializer = ProductSerializer(products)
        return Response(serializer.data)
