from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from user.serializers import UserSerializer, UserNewSerializer
from rest_framework.views import APIView
from django.contrib.auth.models import User


# Create your views here.
class UserView(APIView):
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(
        operation_summary="Добавление нового пользователя",
        responses={
            201: UserSerializer,
            400: "Не правильный ввод данных",
            500: "Серверная ошибка",
        },
        request_body=UserNewSerializer
    )
    def post(self, request):
        user = User.objects.create_user(username=request.data.get('username'),
                                        is_superuser=request.data.get('is_superuser'),
                                        password=request.data.get('password'),
                                        is_staff=request.data.get('is_staff')
                                        )
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @swagger_auto_schema(
        operation_summary="Получение списка всех юзеров",
        responses={200: UserSerializer(many=True), 500: "Серверная ошибка"},
    )
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(
        operation_summary="Получение информации о конкретном юзере",
        responses={200: UserSerializer, 500: "Серверная ошибка"},
    )
    def get(self, request, pk):
        carts = User.objects.filter(pk=pk).first()
        serializer = UserSerializer(carts)
        return Response(serializer.data)

    @swagger_auto_schema(
        operation_summary="Изменение данных юзера",
        responses={
            200: UserSerializer,
            400: "Не правильный ввод данных",
            500: "Серверная ошибка",
        },
        request_body=UserSerializer
    )
    def put(self, request, pk):
        user = User.objects.filter(pk=pk).first()
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Удаление юзера",
        responses={204: UserSerializer, 500: "Серверная ошибка"},
    )
    def delete(self, request, pk):
        users = User.objects.filter(pk=pk).first()
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
