from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from user.models import Users
from user.serializers import UserSerializer
from rest_framework.views import APIView


# Create your views here.
class UserList(APIView):
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(
        operation_summary="Добавление нового пользователя",
        responses={
            201: UserSerializer(many=True),
            400: "Не правильный ввод данных",
            500: "Серверная ошибка",
        },
        request_body=UserSerializer
    )
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Получение списка всех юзеров",
        responses={200: UserSerializer(many=True), 500: "Серверная ошибка"},
    )
    def get(self, request, format=None):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class UserDetail(APIView):
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(
        operation_summary="Получение информации о конкретном юзере",
        responses={200: UserSerializer, 500: "Серверная ошибка"},
    )
    def get(self, request, pk, format=None):
        carts = Users.objects.filter(pk=pk).first()
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
    def put(self, request, pk, format=None):
        users = Users.objects.filter(pk=pk).first()
        serializer = UserSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_summary="Удаление юзера",
        responses={204: UserSerializer, 500: "Серверная ошибка"},
    )
    def delete(self, request, pk, format=None):
        users = Users.objects.filter(pk=pk).first()
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
