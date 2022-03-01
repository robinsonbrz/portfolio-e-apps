from django.contrib import admin

from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "sobrenome", "telefone", "email", "data_criacao", "descricao", "categoria", "mostrar") # noqa E501
    list_display_links = ("id", "nome", "sobrenome")
    # adiciona filtro area administrativa Contatos
    # list_filter = (["categoria"])

    # limita a quantidade de contatos por pagina
    list_per_page = 10

    # Insere campos de pesquisa
    search_fields = ("nome", "sobrenome", "telefone")

    # Permite a edição sem precisar entrar em detalhes
    list_editable = ("telefone", "mostrar")


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
