# Generated by Django 4.1.2 on 2022-10-23 15:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pjgplantas", "0063_remove_itenscarrinho_planta"),
    ]

    operations = [
        migrations.DeleteModel(
            name="PedidoCarrinho",
        ),
    ]
