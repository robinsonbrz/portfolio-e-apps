from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import PortfolioDetail


@admin.register(PortfolioDetail)
class PortDetailAdmin(SummernoteModelAdmin):
    list_display = ('id', 'titulo', 'slug', 'descricao')
    prepopulated_fields = {"slug":("titulo",)}
    summernote_fields = ('descricao', 'detalhe')


# As duas linha abaixo cumprem a mesma tarefa ou decorator ou declarativa
# @admin.register(PortfolioDetail)
# admin.site.register(PortfolioDetail)

#admin.site.register(PortfolioDetail, PortfolioDetailAdmin)


