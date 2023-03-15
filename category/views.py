from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from category.models import Category
from category.serializers import CategorySerializer
from rest_framework.views import APIView


class CategoryList(APIView):
    @swagger_auto_schema(
        operation_summary="Получение списка всех существующих категорий",
        responses={200: CategorySerializer(many=True), 500: "Серверная ошибка"},
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
        products = Category.objects.all()
        serializer = CategorySerializer(products, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Добавление новой категории",
        responses={
            201: CategorySerializer(many=True),
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
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriesProduct(APIView):
    @swagger_auto_schema(
        operation_summary="Получение всех товаров находящихся в определенной категории",
        responses={200: CategorySerializer(many=True), 500: "Серверная ошибка"},
        manual_parameters=[
            openapi.Parameter(
                name="name",
                in_=openapi.IN_QUERY,
                required=True,
                type=openapi.TYPE_STRING,
            )
        ],
    )
    def get(self, request, category_id, format=None):
        products = Category.objects.filter(category_id=category_id)
        serializer = CategorySerializer(products, many=True)
        return Response(serializer.data)
