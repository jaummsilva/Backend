from symtable import Class
from django.contrib import admin

from pjgplantas.models import (
    Boleto,
    Cartao,
    Comentario,
    ItensCarrinho,
    PedidoCarrinho,
    Pix,
    Planta,
)

admin.site.register(Planta)
admin.site.register(Boleto)
admin.site.register(Cartao)
admin.site.register(Pix)
admin.site.register(ItensCarrinho)
admin.site.register(PedidoCarrinho)
admin.site.register(Comentario)
