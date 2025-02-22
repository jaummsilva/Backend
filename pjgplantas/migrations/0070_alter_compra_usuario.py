# Generated by Django 4.1.3 on 2022-12-05 08:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        (
            "pjgplantas",
            "0069_remove_itenscompra_valor_alter_compra_complemento_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="compra",
            name="usuario",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="compras",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
