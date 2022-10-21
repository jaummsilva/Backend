from dataclasses import fields
from pyexpat import model
from rest_framework.serializers import ModelSerializer, SlugRelatedField
from rest_framework import serializers
from media.models import Image
from media.serializers import ImageSerializer
from pjgplantas.models import (
    Boleto,
    Cartao,
    Comentario,
    ItensCarrinho,
    PedidoCarrinho,
    Pix,
    Planta,
)
from django.contrib.auth.models import User


class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)
    password_confirmation = serializers.CharField(max_length=150, write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "password",
            "password_confirmation",
        )

    def validate(self, args):
        email = args.get("email", None)
        username = args.get("username", None)
        password = args.get("password")
        password_confirmation = args.get("password_confirmation")
        if password != password_confirmation:
            raise serializers.ValidationError(
                {"password": ("passwords does not match")}
            )
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": ("email already exists")})
        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError({"username": ("username already exists")})

        return super().validate(args)

    def create(self, validated_data):
        validated_data.pop("password_confirmation")
        return User.objects.create_user(**validated_data)


class ComentarioSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ("id", "texto", "usuario", "planta")


class ComentarioEmPlantaSerializer(ModelSerializer):
    usuario = serializers.CharField(source="usuario.username")

    class Meta:
        model = Comentario
        fields = ("id", "texto", "usuario")


class PlantaSerializer(ModelSerializer):
    class Meta:
        model = Planta
        fields = "__all__"

    imagem_attachment_key = SlugRelatedField(
        source="capa",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    imagem = ImageSerializer(required=False, read_only=True)
    comentarios = ComentarioEmPlantaSerializer(many=True, read_only=True)


# class PlantaDetailSerializer(ModelSerializer):
#     comentarios = PlantaSerializer(source="comentarios_set", many=True)

#     class Meta:
#         model = Comentario
#         fields = ("comentarios",)


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
        fields = (
            "valor",
            "cpf",
            "rg",
            "endereco",
            "complemento",
            "boleto1",
            "cartao1",
            "pix",
            "usuario",
        )


class ItensCarrinhoSerializer(ModelSerializer):
    class Meta:
        model = ItensCarrinho
        fields = ("id", "planta", "preco")


class ComentarioDetailSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ("id", "texto", "usuario", "planta")
        depth = 1
