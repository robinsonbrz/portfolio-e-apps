import json
from datetime import datetime

import requests


def cria_lista_de_cotacoes_por_qtd_dias(par_moedas, qtd_dias):
    objeto_cotacoes = requests.get(f'https://economia.awesomeapi.com.br/json/daily/{par_moedas}/{qtd_dias}')
    # retorna todas as modedas disponíveis para análise
    objeto_cotacoes = objeto_cotacoes.json()

    # Exemplo de retorno
    # {'high': '5.1619', 'low': '5.0784', 'varBid': '0.0845', 'pctChange': '1.66', 'bid': '5.1611', 'ask': '5.1626', 'timestamp': '1652129998'}
    dict_cotacoes = {}
    lista_cotacoes = []
    lista_datas = []
    nome_moeda = objeto_cotacoes[0]['name'].split('/')[0]

    for i , cotacao in enumerate(objeto_cotacoes):
        time_data = datetime.fromtimestamp(int(objeto_cotacoes[i]['timestamp']))
        lista_datas.append(time_data.strftime("%d/%m/%y"))       

    for i , cotacao in enumerate(objeto_cotacoes):
        lista_cotacoes.append(objeto_cotacoes[i]['bid'])

    dict_cotacoes = dict({
            "lista_cotacoes": list(reversed(lista_cotacoes)), 
            "lista_datas": list(reversed(lista_datas)),
            "nome_moeda": nome_moeda
        })

    return dict_cotacoes


def cria_lista_todos_pares_nomes():
    objeto_cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
    # retorna todas as modedas disponíveis
    dict_cotacoes_moedas = objeto_cotacoes.json()

    lista_moedas = []
    dict_pares_moedas = {}
    lista_pares = []

    # itera mostrando todas as moedas possíveis
    for moeda in dict_cotacoes_moedas:
        lista_moedas.append(moeda)
    for moeda in lista_moedas:
        lista_pares.append((moeda,dict_cotacoes_moedas[moeda]['name'].split('/')[0]))
    dict_pares_moedas['pares'] = lista_pares
    return dict_pares_moedas


def cotacao_atual(par_moedas):
    objeto_cotacao = requests.get(f'https://economia.awesomeapi.com.br/last/{par_moedas}')
    # retorna todas as modedas disponíveis para análise
    # print(objeto_cotacoes.status_code)
    objeto_cotacao = objeto_cotacao.json()
    '''
    {"USDBRLT":
    {"code":"USD","codein":"BRLT","name":"Dólar Americano/Real Brasileiro Turismo",
    "high":"5.185","low":"5.12","varBid":"0.01","pctChange":"0.19",
    "bid":"5.01","ask":"5.32","timestamp":"1652296980",
    "create_date":"2022-05-11 16:23:00"}}
    '''
    dict_cotacao = {}
    for par in objeto_cotacao:
        dict_cotacao['par_atual'] = objeto_cotacao[par]
    dict_cotacao['par_atual']['name'] = dict_cotacao['par_atual']['name'].split('/')[0]
    return dict_cotacao


def cotacao_atual_todas():
    dict_pares_moedas = cria_lista_todos_pares_nomes()
    string_pares = ''
    for moeda in dict_pares_moedas['pares']:
        string_pares += moeda[0] + ','
    string_pares = string_pares[:-1]   # retira a última vírgula

    # consulta a api
    # https://economia.awesomeapi.com.br/last/USD,USDT,CAD,EUR,GBP,ARS,BTC,LTC,JPY,CHF,AUD,CNY,ILS,ETH,XRP,DOGE
    objetos_ultima_cotacao = requests.get(f'https://economia.awesomeapi.com.br/last/{string_pares}')
    # recebeu todas as modedas disponíveis para análise
    objetos_ultima_cotacao = objetos_ultima_cotacao.json()

    lista_todos_cot_atual = []
    for a in objetos_ultima_cotacao:
        del objetos_ultima_cotacao[a]['codein']
        del objetos_ultima_cotacao[a]['timestamp']
        objetos_ultima_cotacao[a]['name'] = objetos_ultima_cotacao[a]['name'].split('/')[0]
        objetos_ultima_cotacao[a]['create_date'] = objetos_ultima_cotacao[a]['create_date'][:-3]
        lista_todos_cot_atual.append(objetos_ultima_cotacao[a])
    return lista_todos_cot_atual
