from rest_framework.serializers import ModelSerializer

from pjgplantas.models import Boleto, Cartao, Comentario, ItensCarrinho, Midia, PedidoCarrinho, Pix, Planta, TipoUsuario, Usuario


class TipoUsuarioSerializer(ModelSerializer):
    class Meta:
        model = TipoUsuario
        fields = "__all__"


class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class PlantaSerializer(ModelSerializer):
    class Meta:
        model = Planta
        fields = "__all__"


class BoletoSerializer(ModelSerializer):
    class Meta:
        model = Boleto
        fields = "__all__"


class CartaoSerializer(ModelSerializer):
    class Meta:
        model = Cartao
        fields = "__all__"


class PixSerializer(ModelSerializer):
    class Meta:
        model = Pix
        fields = "__all__"


class PedidoSerializer(ModelSerializer):
    class Meta:
        model = PedidoCarrinho
        fields = "__all__"


class ItensCarrinhoSerializer(ModelSerializer):
    class Meta:
        model = ItensCarrinho
        fields = "__all__"


class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = "__all__"


class MidiaSerializer(ModelSerializer):
    class Meta:
        model = Midia
        fields = "__all__"
