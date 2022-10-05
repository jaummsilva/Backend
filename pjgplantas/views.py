from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

from pjgplantas.models import (
    Boleto,
    Cartao,
    Comentario,
    ItensCarrinho,
    PedidoCarrinho,
    Pix,
    Planta,
)
from pjgplantas.serializers import (
    BoletoSerializer,
    CartaoSerializer,
    ComentarioSerializer,
    ItensCarrinhoSerializer,
    PedidoSerializer,
    PixSerializer,
    PlantaSerializer,
    RegistrationSerializer,
    ComentarioDetailSerializer
)

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        data['email'] = self.user.email

        return data


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class RegistrationViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


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


class PedidoViewSet(ModelViewSet):
    queryset = PedidoCarrinho.objects.all()
    serializer_class = PedidoSerializer


class ItensCarrinhoViewSet(ModelViewSet):
    queryset = ItensCarrinho.objects.all()
    serializer_class = ItensCarrinhoSerializer


class ComentarioViewSet(ModelViewSet):
    queryset = Comentario.objects.all()

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return ComentarioDetailSerializer
        return ComentarioSerializer


