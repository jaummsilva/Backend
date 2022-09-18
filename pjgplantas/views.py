from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User

from pjgplantas.models import (
    Boleto,
    Cartao,
    Comentario,
    ItensCarrinho,
    Midia,
    PedidoCarrinho,
    Pix,
    Planta,
    TipoUsuario,
    Usuario,
)
from pjgplantas.serializers import (
    BoletoSerializer,
    CartaoSerializer,
    ComentarioSerializer,
    ItensCarrinhoSerializer,
    MidiaSerializer,
    PedidoSerializer,
    PixSerializer,
    PlantaSerializer,
    RegistrationSerializer,
    TipoUsuarioSerializer,
    UsuarioSerializer,
)


class RegistrationViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer


class TipoUsuarioViewSet(ModelViewSet):
    queryset = TipoUsuario.objects.all()
    serializer_class = TipoUsuarioSerializer


class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


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
    serializer_class = ComentarioSerializer


class MidiaViewSet(ModelViewSet):
    queryset = Midia.objects.all()
    serializer_class = MidiaSerializer
