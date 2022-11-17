from django.db import models
from django.contrib.auth.models import User
from media.models import Image
from django.utils import timezone
from django.db.models import F


class Planta(models.Model):
    tipo_planta = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    nome = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    imagem = models.ForeignKey(
        Image,
        related_name="+",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        default=None,
    )

    def __str__(self):
        return self.nome


class Boleto(models.Model):
    nome = models.CharField(max_length=150)

    def __str__(self):
        return self.nome


class Cartao(models.Model):
    numero = models.CharField(max_length=19)
    cvv = models.CharField(max_length=3)
    validade = models.CharField(max_length=5)
    nometitular = models.CharField(max_length=100)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nometitular} ({self.numero})"


class Pix(models.Model):
    banco = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=18)
    email = models.EmailField()

    def __str__(self):
        return self.banco


class Comentario(models.Model):
    texto = models.TextField()
    dth = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    planta = models.ForeignKey(
        Planta, on_delete=models.CASCADE, related_name="comentarios"
    )

    def __str__(self):
        return f"{self.usuario} ({self.planta})"


class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, related_name="compras")
    cpf = models.CharField(max_length=14, null=True)
    rg = models.CharField(max_length=9, null=True)
    endereco = models.CharField(max_length=150, null=True)
    complemento = models.CharField(max_length=100, null=True)
    boleto = models.ForeignKey(Boleto, on_delete=models.PROTECT, blank=True, null=True)
    cartao = models.ForeignKey(Cartao, on_delete=models.PROTECT, blank=True, null=True)
    pix = models.ForeignKey(Pix, on_delete=models.PROTECT, blank=True, null=True)

    @property
    def total(self):
        queryset = self.itens.all().aggregate(
            total=models.Sum(F("quantidade") * F("planta__preco"))
        )
        return queryset["total"]

    @property
    def total_compra(self):
        queryset = self.itens.all().aggregate(total=models.Sum(F("total") + F("total")))
        return queryset["total_compra"]


class ItensCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name="itens")
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE, related_name="+")
    quantidade = models.IntegerField()
