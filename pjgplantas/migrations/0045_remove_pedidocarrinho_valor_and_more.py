# Generated by Django 4.1.2 on 2022-10-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pjgplantas", "0044_rename_itencarrinho_pedidocarrinho_itenscarrinho"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pedidocarrinho",
            name="valor",
        ),
        migrations.AlterField(
            model_name="itenscarrinho",
            name="preco",
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
    ]
