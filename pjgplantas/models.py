from django.db import models
from django.contrib.auth.models import User


class Planta(models.Model):
    tipo_planta = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    nome = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)

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
    cnpj = models.CharField(max_length=14)
    email = models.EmailField()

    def __str__(self):
        return self.banco


class PedidoCarrinho(models.Model):
    valor = models.DecimalField(max_digits=9, decimal_places=2)
    quantidade_itens = models.IntegerField()
    dth = models.DateTimeField()
    boleto1 = models.ForeignKey(Boleto, on_delete=models.PROTECT, blank=True, null=True)
    cartao1 = models.ForeignKey(Cartao, on_delete=models.PROTECT, blank=True, null=True)
    pix = models.ForeignKey(Pix, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return f"{self.pedido} ({self.valor})"


class ItensCarrinho(models.Model):
    planta = models.ManyToManyField(
        Planta,
    )
    pedido = models.ForeignKey(PedidoCarrinho, on_delete=models.PROTECT)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    qnt_item = models.IntegerField()
    endereco = models.CharField(max_length=200)
    complemento = models.CharField(max_length=50)


class Comentario(models.Model):
    texto = models.TextField(max_length=500)
    dth = models.DateTimeField()
    comentario2 = models.ForeignKey(Planta, on_delete=models.PROTECT)


class Midia(models.Model):
    local = models.ImageField()
    titulo = models.CharField(max_length=150)
    planta = models.ForeignKey(Planta, on_delete=models.PROTECT)
