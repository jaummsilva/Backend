# Generated by Django 4.1.2 on 2022-10-21 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pjgplantas", "0045_remove_pedidocarrinho_valor_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="itenscarrinho",
            name="qnt_item",
        ),
    ]
