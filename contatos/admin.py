from django.contrib import admin

from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = ("id","nome", "sobrenome", "telefone", "email", "data_criacao", "descricao","categoria")
    list_display_links = ("id","nome", "sobrenome")
    list_filter = ("nome", "sobrenome")
    list_per_page = 20                                  # limita a quantidade de contatos por pagina
    search_fields = ("nome", "sobrenome", "telefone")   # Insere campos de pesquisa


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
