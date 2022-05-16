from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import PortfolioDetail, Testemunhos


@admin.register(PortfolioDetail)
class PortDetailAdmin(SummernoteModelAdmin):
    list_display = ('id', 'titulo', 'slug', 'descricao')
    prepopulated_fields = {"slug":("titulo",)}
    summernote_fields = ('descricao', 'detalhe')


@admin.register(Testemunhos)
class TestemunhosAdmin(admin.ModelAdmin):
    list_display = ('testemunho_nome', 'titulo')


# As duas linha abaixo cumprem a mesma tarefa ou decorator ou declarativa
# @admin.register(PortfolioDetail)
# admin.site.register(PortfolioDetail)

#admin.site.register(PortfolioDetail, PortfolioDetailAdmin)


