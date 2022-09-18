from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from pjgplantas.models import Boleto, Cartao, Comentario, ItensCarrinho, Midia, PedidoCarrinho, Pix, Planta, TipoUsuario, Usuario
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)
    password_confirmation = serializers.CharField(
        max_length=150, write_only=True)

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email',
                  'username', 'password', 'password_confirmation')

    def validate(self, args):
        email = args.get('email', None)
        username = args.get('username', None)
        password = args.get('password')
        password_confirmation = args.get('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError(
                {'password': ('passwords does not match')})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                {'email': ('email already exists')})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {'username': ('username already exists')})

        return super().validate(args)

    def create(self, validated_data):
        validated_data.pop('password_confirmation')
        return User.objects.create_user(**validated_data)


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
