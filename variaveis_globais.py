import flet as ft
import banco as bd
import icons as ic
import colors as c
import unicodedata
from decimal import Decimal
import dicionario_idioma as dic

def sistema_de_busca(e, page: ft.Page, lista_de_controls = None, dicionario_controls_carregados = None):
    if lista_de_controls == None or dicionario_controls_carregados == None:
        print('Falta lista ou dicionario')
        return None
    
    digitado = e.control.value
    if digitado == '':
        print('campo caiu no vazio')
        if len(lista_de_controls.controls) < len(dicionario_controls_carregados):
            print('controles caiu no menor numemro')
            lista_de_controls.controls.clear()
            for x in dicionario_controls_carregados:
                print('adicionado')
                lista_de_controls.controls.append(dicionario_controls_carregados[x])

        page.update()

        return
    lista_de_controls.controls.clear()
    controles = []

    def normalizar_letras(texto):
        texto = unicodedata.normalize('NFD', texto)
        texto = ''.join(
            letra
            for letra in texto
            if unicodedata.category(letra) != 'Mn'
        )
        return texto.lower()
    
    palavras_busca = normalizar_letras(digitado).split()

    for servico in dicionario_controls_carregados:
        texto_servico = normalizar_letras(servico)
        if all(palavra in texto_servico for palavra in palavras_busca):
            lista_de_controls.alignment = ft.MainAxisAlignment.START
            controles.append(dicionario_controls_carregados[servico])

    if len(controles) == 0:
        not_found = ft.Column(
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                ic.svg_icon(
                    'not_found_busca',
                    size = 50, color = c.texto_principal
                ),
                ft.Text(
                    value = dic.palavras[dic.idioma_select]['atendimento']['sem_resultados'],
                    size = 16, color = c.texto_principal,
                    font_family = 'inter', text_align = ft.TextAlign.CENTER
                ),
            ]
        )

        lista_de_controls.alignment = ft.MainAxisAlignment.CENTER
        lista_de_controls.controls.append(not_found)
        return
    
    lista_de_controls.controls.extend(controles)
    page.update()
def barra_pesquisa(
    text_interno = dic.palavras[dic.idioma_select]['atendimento']['busca_rapida'],

    on_blur: ft.Event = None,
    on_focus: ft.Event = None,
    on_change: ft.Event = None,
):
    return ft.Stack(
        height = 78,
        expand = True,
        alignment = ft.Alignment.CENTER,
        controls = [
            ft.Container(
                left = 0,
                right = 0,
                expand = True,
                bgcolor = c.fundo_neutralo,
                border_radius = 28,
                shadow = c.shadow_leve(),
                
                margin = ft.Margin(
                    left = margin_left
                ),

                content = ft.TextField(
                    expand = True,
                    border_radius = 28,
                    content_padding = ft.Padding(top = 24.5, left = 64, bottom = 24.5),
                    bgcolor = c.fundo_neutralo,
                    border_color = ft.Colors.TRANSPARENT,
                    focused_border_color = c.cor_principal,

                    text_style = ft.TextStyle(
                        size = 16, color = c.texto_principal,
                        font_family = 'inter'
                    ),

                    hint_text = text_interno,
                    hint_style = ft.TextStyle(
                        size = 16, color = c.texto_suave,
                        font_family = 'inter'
                    ),

                    text_align = ft.TextAlign.START,
                    on_blur = on_blur,
                    on_focus = on_focus,
                    on_change = on_change,
                )
            ),
            
            ic.svg_icon(
                icon = 'lupa',
                size = 30, color = c.texto_suave,
                left = 38, top = 0, bottom = 0
            )
        ]
    )

box_PopUp = ft.Stack(
    expand = True,
    visible = False,
    alignment = ft.Alignment.CENTER,
    controls = [
        ft.Container(
            expand = True,
            bgcolor = ft.Colors.with_opacity(color = ft.Colors.BLACK, opacity = 0.3)
        ),
        ft.Container(
            border_radius = 34,
            shadow = c.shadow_leve(),
            bgcolor = c.fundo_neutralo,
            alignment = ft.Alignment.CENTER,
            margin = ft.Margin(
                top = 98,
                left = 24,
                right = 24,
                bottom = 98
            ),
        )
    ]
)

def conteudo_box_PopUp(page: ft.Page, conteudo = None):
    box_PopUp.controls[1].content = conteudo
    page.update()

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




