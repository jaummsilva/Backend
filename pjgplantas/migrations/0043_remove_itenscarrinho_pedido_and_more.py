# Generated by Django 4.1.2 on 2022-10-21 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pjgplantas", "0042_alter_cartao_cvv"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="itenscarrinho",
            name="pedido",
        ),
        migrations.AddField(
            model_name="pedidocarrinho",
            name="itencarrinho",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="pjgplantas.itenscarrinho",
            ),
            preserve_default=False,
        ),
    ]
