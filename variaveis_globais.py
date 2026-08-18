import banco as bd
import flet as ft
from decimal import Decimal

moeda_ativa = 'BR'
margin_left = 16
margin_right = 16
margin_top = 16

servicos_carregados = {}

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

async def scrollagem(column_row, key = None, time = 300, offset = None):
    await column_row.scroll_to(
        offset = offset,
        scroll_key = key,
        duration = time
    )

armazenamento_totais_p_servico = {}
totais = 0.00

mudar_button_config_EXIT_MENU = None
click_cor_control_bar = None
titulo_control = None
tela_anterior = None
area_page = None
page = None

async def troca_tela(e, nova_tela_go = None, anterior = False, titulo = None):
    global page
    global area_page
    global tela_anterior
    global titulo_control
    global click_cor_control_bar
    global mudar_button_config_EXIT_MENU

    mudar_button_config_EXIT_MENU()
    click_cor_control_bar(e, controle = titulo)
    nova_tela_GO = await nova_tela_go.tela()
    titulo_control.value = titulo

    area_page.controls.clear()
    area_page.controls.append(nova_tela_GO)
    
    if anterior:
        tela_anterior = nova_tela_GO

    page.update()







