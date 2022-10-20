# Generated by Django 4.1.2 on 2022-10-20 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("pjgplantas", "0039_remove_itenscarrinho_complemento_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="cartao",
            name="usuario",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
