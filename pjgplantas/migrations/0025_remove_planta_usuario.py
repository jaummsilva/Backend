# Generated by Django 4.0.6 on 2022-09-18 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pjgplantas', '0024_remove_itenscarrinho_planta_itenscarrinho_planta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='planta',
            name='usuario',
        ),
    ]
