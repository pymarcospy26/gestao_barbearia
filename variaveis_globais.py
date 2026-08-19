import flet as ft
import banco as bd
from decimal import Decimal
import dicionario_idioma as dic

moeda_ativa = dic.idioma_select
margin_left = 16
margin_right = 16
margin_top = 16

moedas_format = {
    'BR': ['0,00', 'R$ 1.234,56', '.', ',', 0, 'R$ '],
    'ES': ['0,00', '1.234,56 €', '.', ',', -1, ' €'],
    'FR': ['0,00', '1 234,56 €', ' ', ',', -1, ' €'],
    'EUA': ['0.00', '$ 1,234.56', ',', '.', 0, '$ '],
}

servicos_carregados = {}
subtotal = 0

async def carregar_dados():
    conexao = await bd.servico_valor()

    for servico in conexao:
        setor = servico[0]
        produto = servico[1]
        valor = servico[2]

        if setor not in servicos_carregados:
            servicos_carregados[setor] = {}

        if 'todos' not in servicos_carregados:
            servicos_carregados['todos'] = {}

        servicos_carregados[setor][produto] = {'setor': setor, 'produto': produto, 'valor': valor}
        servicos_carregados['todos'][produto] = {'setor': setor, 'produto': produto, 'valor': valor}

pagina_main = None
pagina_home = None
pagina_idioma = None
pagina_configuracao_main = None
pagina_agenda = None
pagina_atendimento = None
cor_btns_navegation_bar = None

def decimal_n(valor = None, texto = False, moeda = None):
    if valor == None: return
    else:
        try:
            formatacao = Decimal(str(valor)).quantize(Decimal('0.01'))
            if texto == False:
                return formatacao
            else:
                formatacao = str(formatacao)
                return formatacao

        except Exception as err: print('NÂO FOI POSSÍVEL CONVERTER DECIMAL.\nERRO:\n', err)

async def scrollagem_key(column_row, key = None, time = 260):
    await column_row.scroll_to(
        scroll_key = key,
        duration = time,
    )

armazenamento_totais_p_servico = {}
totais = 0.00

tela_anterior = None
troca_de_pagina = None

page_croll_main = None
area_page_main = None
pagina_atendimento_go = None
pagina_pagamento_go = None
pagina_ativa_go = None
btn_centro = None
go_pagamento_aprovd = False
nova_tela_atendimento = None

def limpar_globais():
    global servicos_carregados
    global subtotal

    global pagina_main
    global pagina_home
    global pagina_idioma
    global pagina_configuracao_main
    global pagina_agenda
    global pagina_atendimento
    global cor_btns_navegation_bar

    global armazenamento_totais_p_servico
    global totais
    global tela_anterior
    global troca_de_pagina

    global page_croll_main
    global area_page_main
    global pagina_atendimento_go
    global pagina_pagamento_go
    global pagina_ativa_go
    global btn_centro
    global go_pagamento_aprovd
    global nova_tela_atendimento

    servicos_carregados = {}
    subtotal = 0

    pagina_main = None
    pagina_home = None
    pagina_idioma = None
    pagina_configuracao_main = None
    pagina_agenda = None
    pagina_atendimento = None
    cor_btns_navegation_bar = None
    
    armazenamento_totais_p_servico = {}
    totais = 0.00

    tela_anterior = None
    troca_de_pagina = None

    page_croll_main = None
    area_page_main = None
    pagina_atendimento_go = None
    pagina_pagamento_go = None
    pagina_ativa_go = None
    btn_centro = None
    go_pagamento_aprovd = False
    nova_tela_atendimento = None




