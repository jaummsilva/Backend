# Generated by Django 4.1.2 on 2022-10-23 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pjgplantas", "0054_compra_boleto"),
    ]

    operations = [
        migrations.RenameField(
            model_name="pedidocarrinho",
            old_name="pix",
            new_name="pix1",
        ),
    ]
