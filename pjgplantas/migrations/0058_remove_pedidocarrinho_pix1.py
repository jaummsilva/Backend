# Generated by Django 4.1.2 on 2022-10-23 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pjgplantas", "0057_remove_pedidocarrinho_itenscarrinho"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pedidocarrinho",
            name="pix1",
        ),
    ]
