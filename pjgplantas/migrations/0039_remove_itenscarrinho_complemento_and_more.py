# Generated by Django 4.1.2 on 2022-10-20 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pjgplantas", "0038_remove_pedidocarrinho_quantidade_itens_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="itenscarrinho",
            name="complemento",
        ),
        migrations.RemoveField(
            model_name="itenscarrinho",
            name="endereco",
        ),
    ]
