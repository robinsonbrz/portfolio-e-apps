from django.contrib import admin

from .models import PortfolioDetail


@admin.register(PortfolioDetail)
class PortDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'slug', 'descricao')
    prepopulated_fields = {"slug":("titulo",)}


# As duas linha abaixo cumprem a mesma tarefa ou decorator ou declarativa
# @admin.register(PortfolioDetail)
# admin.site.register(PortfolioDetail)
