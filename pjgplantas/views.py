from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

from pjgplantas.models import Boleto, Cartao, Comentario, Pix, Planta, Compra
from pjgplantas.serializers import (
    BoletoSerializer,
    CartaoSerializer,
    ComentarioSerializer,
    PixSerializer,
    PlantaSerializer,
    RegistrationSerializer,
    ComentarioDetailSerializer,
    CriarEditarCompraSerializer,
    CompraSerializer,
)

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data["username"] = self.user.username
        data["email"] = self.user.email
        data["first_name"] = self.user.first_name
        data["last_name"] = self.user.last_name
        data["id"] = self.user.id
        data["password"] = self.user.password
        data["is_superuser"] = self.user.is_superuser
        data["compras"] = self.user.compras.all()

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegistrationViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class PlantaViewSet(ModelViewSet):
    queryset = Planta.objects.all()
    serializer_class = PlantaSerializer


class BoletoViewSet(ModelViewSet):
    queryset = Boleto.objects.all()
    serializer_class = BoletoSerializer


class CartaoViewSet(ModelViewSet):
    queryset = Cartao.objects.all()
    serializer_class = CartaoSerializer


class PixViewSet(ModelViewSet):
    queryset = Pix.objects.all()
    serializer_class = PixSerializer


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ComentarioDetailSerializer
        return ComentarioSerializer


class CompraViewSet(ModelViewSet):
    queryset = Compra.objects.all()

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return CompraSerializer
        return CriarEditarCompraSerializer
