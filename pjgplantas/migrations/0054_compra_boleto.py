# Generated by Django 4.1.2 on 2022-10-23 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("pjgplantas", "0053_compra_complemento_compra_endereco_compra_rg"),
    ]

    operations = [
        migrations.AddField(
            model_name="compra",
            name="boleto",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="pjgplantas.boleto",
            ),
        ),
    ]
