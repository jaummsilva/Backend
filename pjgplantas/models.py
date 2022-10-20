from django.db import models
from django.contrib.auth.models import User
from media.models import Image
from django.utils import timezone


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
    cvv = models.IntegerField()
    validade = models.DateField()
    nometitular = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nometitular} ({self.numero})"


class Pix(models.Model):
    banco = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=18)
    email = models.EmailField()

    def __str__(self):
        return self.banco


class PedidoCarrinho(models.Model):
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    dth = models.DateTimeField()
    cpf = models.CharField(max_length=14)
    rg = models.CharField(max_length=9)
    endereco = models.CharField(max_length=150)
    complemento = models.CharField(max_length=100)
    boleto1 = models.ForeignKey(Boleto, on_delete=models.PROTECT, blank=True, null=True)
    cartao1 = models.ForeignKey(Cartao, on_delete=models.PROTECT, blank=True, null=True)
    pix = models.ForeignKey(Pix, on_delete=models.PROTECT, blank=True, null=True)
    usuario = models.ForeignKey(User,on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.usuario} ({self.valor})"


class ItensCarrinho(models.Model):
    planta = models.ManyToManyField(
        Planta,
    )
    pedido = models.ForeignKey(PedidoCarrinho, on_delete=models.PROTECT)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    qnt_item = models.IntegerField()


class Comentario(models.Model):
    texto = models.TextField()
    dth = models.DateTimeField(default=timezone.now)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    planta = models.ForeignKey(
        Planta, on_delete=models.PROTECT, related_name="comentarios"
    )

    def __str__(self):
        return f"{self.usuario} ({self.planta})"
