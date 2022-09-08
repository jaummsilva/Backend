from django.contrib import admin

from pjgplantas.models import Boleto, Cartao, Comentario, ItensCarrinho, Midia, PedidoCarrinho, Pix, Planta, TipoUsuario, Usuario

admin.site.register(Usuario)
admin.site.register(TipoUsuario)
admin.site.register(Planta)
admin.site.register(Boleto)
admin.site.register(Cartao)
admin.site.register(Pix)
admin.site.register(PedidoCarrinho)
admin.site.register(ItensCarrinho)
admin.site.register(Comentario)
admin.site.register(Midia)
