from symtable import Class
from django.contrib import admin

from pjgplantas.models import (
    Boleto,
    Cartao,
    Comentario,
    Pix,
    Planta,
    Compra,
    ItensCompra
)

admin.site.register(Planta)
admin.site.register(Boleto)
admin.site.register(Cartao)
admin.site.register(Pix)
admin.site.register(Comentario)


class ItensInline(admin.TabularInline):
    model = ItensCompra


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = (ItensInline,)
