# import numpy as np
# import pandas as pd
from django.shortcuts import render

import charts.le_cotacoes as lc
import charts.payoff_utils as pu


def home(request):
    # valores padrao caso não receba parametros GET
    # nome_moeda = 'Bitcoin'
    par_moedas = 'USD-BRL'
    dias = '60'

    # par_moedas = 
    if 'par_moedas_form' in request.GET:
        par_moedas = request.GET['par_moedas_form']
    if 'dias_form' in request.GET:
        dias = request.GET['dias_form']

    dict_cotacoes = lc.cria_lista_de_cotacoes_por_qtd_dias(par_moedas, dias)
    dict_cotacoes['par_moedas'] = par_moedas
    dict_cotacoes['qtd_dias'] = dias

    dict_cotacoes.update(lc.cria_lista_todos_pares_nomes())
    dict_cotacoes.update(lc.cotacao_atual(par_moedas))
    
    # concatena lista de todas as cotações
    dict_cotacoes['lista_todos_cot_atual'] = lc.cotacao_atual_todas()
    # print(dict_cotacoes)

    return render(request, 'charts/pages/home.html', context = dict_cotacoes)

    
