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
    Pix,
    Planta,
    Compra,
    ItensCompra,
)

from django.contrib.auth.models import User


class ItensCompraSerializer(ModelSerializer):
    total = serializers.SerializerMethodField()

    class Meta:
        model = ItensCompra
        fields = (
            "planta",
            "quantidade",
            "total",
        )
        depth = 2

    def get_total(self, instance):
        return instance.quantidade * instance.planta.preco

    def get_total_compra(self, instance):
        return instance.total + instance.total


class CompraSerializer(ModelSerializer):
    usuario = serializers.IntegerField(source="usuario.id")
    itens = ItensCompraSerializer(many=True)

    class Meta:
        model = Compra
        fields = "__all__"



class CriarEditarItensCompraSerializer(ModelSerializer):
    class Meta:
        model = ItensCompra
        fields = ("planta", "quantidade")


class CriarEditarCompraSerializer(ModelSerializer):
    itens = CriarEditarItensCompraSerializer(many=True)
    usuario = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Compra
        fields = ("id", "usuario", "itens")

    def create(self, validated_data):
        itens = validated_data.pop("itens")
        compra = Compra.objects.create(**validated_data)
        for item in itens:
            ItensCompra.objects.create(compra=compra, **item)
        compra.save()
        return compra

    def update(self, instance, validated_data):
        itens = validated_data.pop("itens")
        if itens:
            for item in itens:
                ItensCompra.objects.create(compra=instance, **item)
            instance.save()
        return instance


class RegistrationSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=50, min_length=6)
    username = serializers.CharField(max_length=50, min_length=6)
    password = serializers.CharField(max_length=150, write_only=True)
    password_confirmation = serializers.CharField(
        max_length=150, write_only=True)
    compras = CompraSerializer(many=True)

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
            "compras"
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
        source="imagem",
        queryset=Image.objects.all(),
        slug_field="attachment_key",
        required=False,
        write_only=True,
    )
    imagem = ImageSerializer(required=False, read_only=True)
    comentarios = ComentarioEmPlantaSerializer(many=True, read_only=True)


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


class ComentarioDetailSerializer(ModelSerializer):
    class Meta:
        model = Comentario
        fields = ("id", "texto", "usuario", "planta")
        depth = 1
