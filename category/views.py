from django.http import Http404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from category.models import Category
from category.serializers import CategorySerializer
from rest_framework.views import APIView
from product.models import Product


class CategoryView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @swagger_auto_schema(
        operation_summary="Получение списка всех существующих категорий",
        responses={200: CategorySerializer(many=True), 500: "Серверная ошибка"},
    )
    def get(self, request):
        products = Category.objects.all()
        serializer = CategorySerializer(products, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Добавление новой категории",
        responses={
            201: CategorySerializer,
            400: "Не правильный ввод данных",
            500: "Серверная ошибка",
        },
        request_body=CategorySerializer
    )
    def post(self, request):
        if request.user.is_superuser:
            serializer = CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            raise Http404


class CategoriesProduct(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)

    @swagger_auto_schema(
        operation_summary="Получение всех товаров находящихся в определенной категории",
        responses={200: CategorySerializer(many=True), 500: "Серверная ошибка"},
    )
    def get(self, request, category_id):
        products = Product.objects.filter(category_id=category_id)
        serializer = CategorySerializer(products, many=True)
        return Response(serializer.data)
