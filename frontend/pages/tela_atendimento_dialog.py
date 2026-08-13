import flet as ft
import banco as bd
import icons as ic
import colors as c
import unicodedata
import asyncio
import play_audio as play
from decimal import Decimal
import variaveis_globais as vg

class AlertDialog_atendimento:
    def __init__(
        self, page,
    ):
        self.page = page
        self.titulo = ''

        self.servicos_atendimento = {}
        self.totais = 0
        self.totais_reserva = self.totais
        self.porcentagem_ativa = True
        self.cartao_credito = True
        self.box_cartao_ativo = False

        self.fieldtext_cartao = None
        self.value_taxa_cartao = Decimal("0")
        self.value_fieldtext_cartao = Decimal("0")
        self.taxa_debito_C = Decimal("0.0015")
        self.taxa_credito_C = Decimal("0.0023")
        self.taxa_cartoes = Decimal("0")
        self.coluna_main_descontos_adicionais = None
        self.descontos_Fn = 0
        self.adicionais_Fn = 0
        self.taxa_operacao = 0

        self.margin_lateral_interna = 25
        self.largura_page = self.page.width

        self.dialog_aberto = False

        self.armazenamento_controles = {}
        self.armazenamento_tags = {}

        self.cliente_cadastrados = [
            "João Pedro",
            "Lucas Henrique",
            "Gabriel Silva",
            "Matheus Oliveira",
            "Rafael Costa",
            "Felipe Santos",
            "Bruno Almeida",
            "Carlos Eduardo",
            "Diego Ferreira",
            "Vinícius Souza",
            "Gustavo Lima",
            "André Luiz",
            "Thiago Martins",
            "Leonardo Rocha",
            "Pedro Henrique",
        ]

        self.alertdialog_global = ft.AlertDialog(
            modal = False,
            expand = True,
            actions_padding = 0,
            content_padding = 0,
            bgcolor = c.background,
            shape = ft.RoundedRectangleBorder(radius = 34),
            inset_padding = ft.Padding(left = vg.margin_left, right = vg.margin_right, bottom = 0),

            data = {},
            
            title_padding = ft.Padding(
                left = self.margin_lateral_interna,
                right = self.margin_lateral_interna,
                top = 26,
            )
        )

    @staticmethod
    def decimal_from_value(valor):
        if valor in ['', 'None', None]:
            return Decimal('0')
        if isinstance(valor, Decimal):
            return valor

        texto = str(valor).strip().replace(' ', '').replace('-', '')

        if ',' in texto and '.' in texto:
            if texto.rfind(',') > texto.rfind('.'):
                texto = texto.replace('.', '').replace(',', '.')
            else:
                texto = texto.replace(',', '')
        elif ',' in texto:
            texto = texto.replace('.', '').replace(',', '.')
        elif '.' in texto:
            texto = texto.replace(',', '')

        return Decimal(texto)

    @staticmethod
    def decimal_to_texto(valor):
        if valor in ['', 'None', None]:
            return '0,00'
        valor_decimal = Decimal(str(valor)).quantize(Decimal('0.01'))
        return f'{valor_decimal:.2f}'.replace('.', ',').replace('-', '')

    def adicao_steppers(self, setor, servico, valor):
        stepper = self.stepper_control(
            servico = servico,
            valor = valor,
            text_total = self.alertdialog_global.data['barra_inferior_atendimento'].content.controls[0].controls[1]
        )
                                
        valors = f'R$ {valor:.2f}'.replace('.', ',')

        controle = ft.Container(
            expand = True,
            border_radius = 0,
            border = ft.Border(bottom = ft.BorderSide(width = 0.04, color = c.preto_icons)),
            margin = ft.Margin(left = self.margin_lateral_interna, right = self.margin_lateral_interna),
                                                                    
            data = {
                'setor': setor,
                'servico': servico,
                'valor': valor,
                'stepper': stepper
            },
                                                                        
            content = ft.Row(
                margin = 0,
                height = 84,
                expand = True,
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment = ft.CrossAxisAlignment.CENTER,
                                
                controls = [
                    ft.Column(
                        height = 45,
                        spacing = 0,
                        expand = True,
                        alignment = ft.MainAxisAlignment.CENTER,
                        horizontal_alignment = ft.CrossAxisAlignment.START,
                
                        controls = [
                            ft.Text(
                                expand = True,
                                max_lines = 1,
                                value = servico,
                                overflow = ft.TextOverflow.ELLIPSIS,
                                style = ft.TextStyle(size = 16, color = c.preto_icons, font_family = 'inter'),
                            ),

                            ft.Text(
                                expand = True,
                                max_lines = 1,
                                value = valors,
                                overflow = ft.TextOverflow.ELLIPSIS,
                                style = ft.TextStyle(size = 14, color = c.preto_icons, font_family = 'inter', weight = ft.FontWeight.W_300),
                            )
                        ]
                    ),
                            
                    stepper
                ]
            )
        )
        
        self.alertdialog_global.data['lista_atendimento'].controls.append(controle)
#       AQUI ^ ADICIONA OS CONTROLES/LISTA NA TELA ATRAVÉZ DO DATA DO ALERTDIALOG

        return controle
#       RETORNA O CONTROLE PARA ADICIONÁ-LO A UM DICIONÁRIO DE ARMAZENAMENTO QUANDO A FUNÇÃO É CHAMADA

    def recarregar_lista(self, e):
        botao = e.control
        setor = botao.data['setor']
        lista = self.alertdialog_global.data['lista_atendimento']

        lista.controls.clear()
        lista.alignment = ft.MainAxisAlignment.CENTER
        lista.controls.append(ft.ProgressRing(color = c.lilas_calmo, height = 80, width = 80))

        for tag in self.armazenamento_tags:
            self.armazenamento_tags[tag].bgcolor = c.branco
            self.armazenamento_tags[tag].content.color = c.textos
            self.armazenamento_tags[tag].update()

        botao.bgcolor = c.lilas
        botao.content.color = c.branco

        botao.update()

        async def carregar_nova_lista():
            lista.controls.clear()
            lista.alignment = ft.MainAxisAlignment.START

            for controle in self.armazenamento_controles:       #   BUSCA O ID/SERVICO CONTAINER DENTRO DO DICIONÁRIO
                box = self.armazenamento_controles[controle]    #   ARMAZENA O CONTAINER

                if setor != 'Todos':
                    if box.data['setor'] == setor:
                        lista.controls.append(box)

                else:
                    lista.controls.append(box)
            
            lista.update()
            self.alertdialog_global.data['tags_atendimento'].update()

        self.page.run_task(carregar_nova_lista)

    async def inicializar(self, e = None):
        self.dados_carregados = False

        await self.pages_dialog()

    async def carregar_dados(self):
        setores = await bd.setores()
        servicos_valors = await bd.servico_valor()

        self.alertdialog_global.data['lista_atendimento'].alignment = ft.MainAxisAlignment.START

        self.alertdialog_global.data['lista_atendimento'].controls.clear()

        tag_todos = ft.Container(
            height = 56,
            bgcolor = c.lilas,
            border_radius = 22,
            shadow = c.shadow_leve(),
            alignment = ft.Alignment.CENTER,
            padding = ft.Padding(left = 26, right = 26),
            margin = ft.Margin(left = self.margin_lateral_interna),
                        
            content = ft.Text(
                value = 'Todos',
                style = ft.TextStyle(
                    size = 14, color = c.branco
                )
            ),

            data = {
                'setor': 'Todos'
            },

            on_click = self.recarregar_lista
        )

        self.alertdialog_global.data['tags_atendimento'].controls.append(tag_todos)

        self.armazenamento_tags['Todos'] = tag_todos
        
        for setor in setores[:3]:
            tag = ft.Container(
                height = 54,
                bgcolor = c.branco,
                border_radius = 22,
                shadow = c.shadow_leve(),
                alignment = ft.Alignment.CENTER,
                padding = ft.Padding(left = 26, right = 26),
                data = {
                    'setor': setor
                },
            
                content = ft.Text(
                    value = setor,
                    style = ft.TextStyle(
                        size = 14, color = c.textos
                    )
                ),
                ink = True,
                on_click = self.recarregar_lista
            )

            self.armazenamento_tags[setor] = tag
            self.alertdialog_global.data['tags_atendimento'].controls.append(tag)
            self.alertdialog_global.data['tags_atendimento'].update()
                
        for setor_reserva, servico, valor in servicos_valors:
            controle = self.adicao_steppers(setor_reserva, servico, valor)
            self.armazenamento_controles[controle.data['servico']] = controle
#           AQUI ^ SÃO ADICIONADOS AO DICIONÁRIO OS RETURN'S (CONTROLES) DA DEF DE CONTROLES/LISTA
    
        self.alertdialog_global.data['lista_atendimento'].update()
        self.alertdialog_global.data['tags_atendimento'].update()

        self.dados_carregados = True

    def pesquisa_servicos(self, e):
        digitado = e.control.value
        self.alertdialog_global.data['lista_atendimento'].controls.clear()

        controles = []

        def normalizar_letras(texto):
            texto = unicodedata.normalize('NFD', texto)
            texto = ''.join(
                letra
                for letra in texto
                if unicodedata.category(letra) != 'Mn'
            )

            return texto.lower()

        palavras = normalizar_letras(digitado).split()

        for servico in self.armazenamento_controles:
            texto_servico = normalizar_letras(servico)

            if all(palavra in texto_servico for palavra in palavras):
                self.alertdialog_global.data['lista_atendimento'].alignment = ft.MainAxisAlignment.START
                controles.append(self.armazenamento_controles[servico])

        if len(controles) == 0:
            not_found = ft.Column(
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                controls = [
                    ic.svg_icon(
                        'not_found_busca',
                        size = 50, color = c.preto_icons
                    ),

                    ft.Text(
                        value = 'Sem resultados\npara essa busca',
                        size = 16, color = c.preto_icons,
                        font_family = 'inter', text_align = ft.TextAlign.CENTER
                    ),
                ]
            )

            self.alertdialog_global.data['lista_atendimento'].alignment = ft.MainAxisAlignment.CENTER
            self.alertdialog_global.data['lista_atendimento'].controls.append(not_found)

            return
        
        self.alertdialog_global.data['lista_atendimento'].controls.extend(controles)

    def barra_pesquisa(
        self,
        text_interno = 'Busca rápida',

        on_focus: ft.Event = None,
        on_change: ft.Event = None,
    ):
        return ft.Stack(
            height = 74,
            alignment = ft.Alignment.CENTER,

            controls = [
                ft.Container(
                    left = 0,
                    right = 0,
                    expand = True,
                    bgcolor = c.branco,
                    border_radius = 24,
                    shadow = c.shadow_leve(),
                    
                    margin = ft.Margin(
                        left = self.margin_lateral_interna, right = self.margin_lateral_interna
                    ),

                    content = ft.TextField(
                        expand = True,
                        border_radius = 24,
                        content_padding = ft.Padding(left = 50, top = 21, bottom = 21),

                        bgcolor = c.branco,
                        border_color = ft.Colors.TRANSPARENT,
                        focused_border_color = c.lilas_calmo,

                        text_style = ft.TextStyle(
                            size = 16, color = c.textos,
                            font_family = 'inter'
                        ),

                        hint_text = text_interno,
                        hint_style = ft.TextStyle(
                            size = 16, color = c.sub_textos,
                            font_family = 'inter'
                        ),

                        on_focus = on_focus,
                        on_change = on_change
                    )
                ),
                
                ic.svg_icon(
                    path = 'lupa',
                    size = 30, color = c.sub_textos,
                    left = 38
                )
            ]
        )

    def abrir(self, e = None):
        if self.alertdialog_global.open:
            return

        self.totais = 0
        self.servicos_atendimento.clear()

        self.alertdialog_global.content.height = self.page.height * 3 / 4
        self.alertdialog_global.content.width = self.page.width

        self.dialog_aberto = True

        self.page.show_dialog(self.alertdialog_global)
        self.page.update()

        if not self.dados_carregados:
            self.page.run_task(self.carregar_dados)

    def fechar(self, e = None):
        self.dialog_aberto = False

        self.page.pop_dialog()
        self.page.update()

    def status_quant_stepper(self, e):
        controle = e.control
        servico = controle.data['servico']
        valor = controle.data['valor']
        campo = controle.data['campo']
        btn_inverso = controle.data['btn_inverso']

        quantidade = 0

        if controle.data['acao'] == 'subtrair' and int(campo.value) <= 0:
            return

        if controle.data['acao'] == 'somar':
            if int(campo.value) == 0:
                controle.bgcolor = c.lilas
                controle.content.color = c.branco

                btn_inverso.opacity = 1
                btn_inverso.on_click = self.status_quant_stepper

                btn_inverso.update()
                controle.update()

            quantidade = int(campo.value)
            quantidade += 1

            valor_decimal = self.decimal_from_value(valor)
            self.servicos_atendimento[servico] = {
                'valor': valor_decimal,
                'quantidade': quantidade,
                'total': valor_decimal * Decimal(str(quantidade))
            }

            campo.value = quantidade
            campo.update()

        else:
            quantidade = int(campo.value)
            quantidade = quantidade - 1

            valor_decimal = self.decimal_from_value(valor)
            self.servicos_atendimento[servico] = {
                'valor': valor_decimal,
                'quantidade': quantidade,
                'total': valor_decimal * Decimal(str(quantidade))
            }

            campo.value = quantidade
            campo.update()

            if quantidade == 0:
                btn_inverso.bgcolor = c.branco
                btn_inverso.content.color = c.textos

                controle.on_click = None
                controle.opacity = 0.2

                if servico in self.servicos_atendimento:      #   LIMPA O REGISTRO DO DICIONÁRIO PARA NÃO SER UM PROBLEMA NA H0RA DE LER
                    self.servicos_atendimento.pop(servico)

                controle.update()
                btn_inverso.update()

        totais_temporario = Decimal('0')

        for servicos in self.servicos_atendimento:
            totais_temporario += self.decimal_from_value(self.servicos_atendimento[servicos]['total'])

        self.totais = totais_temporario

        controle.data['text_total'].value = f'R$ {self.decimal_to_texto(totais_temporario)}'

        controle.data['text_total'].update()

        totais_temporario = Decimal('0')

        print(self.totais)
        print(self.servicos_atendimento)
    
    def stepper_control(self, servico = None, valor = None, text_total = ft.Control):
        campo = ft.Text(
            value = 0,
            width = 50,
            max_lines = 1,
            text_align = ft.TextAlign.CENTER,
            overflow = ft.TextOverflow.ELLIPSIS,
        
            style = ft.TextStyle(
                size = 18, color = c.preto_icons, font_family = 'inter'
            )
        )

        btn_menos = ft.Container(          #   BOTÃO DE SUBTRAÇÃO
            width = 54,
            height = 54,
            opacity = 0.2,
            border_radius = 22,
            bgcolor = c.branco,
            shadow = c.shadow_leve(),
            alignment = ft.Alignment.CENTER,
                
            content = ft.Icon(
                icon = ft.CupertinoIcons.MINUS,
                size = 16, color = c.textos
            )
        )

        btn_mais = ft.Container(           #   BOTÃO DE ADIÇÃO
            width = 54,
            height = 54,
            border_radius = 22,
            bgcolor = c.branco,
            shadow = c.shadow_leve(),
            alignment = ft.Alignment.CENTER,
                                    
            content = ft.Icon(
                icon = ft.CupertinoIcons.PLUS,
                size = 16, color = c.textos
            ),

            on_click = self.status_quant_stepper
        )

        btn_mais.data = {
            'servico': servico,
            'valor': valor,
            'campo': campo,
            'btn_inverso': btn_menos,
            'text_total': text_total,

            'acao': 'somar'
        }

        btn_menos.data = {
            'servico': servico,
            'valor': valor,
            'campo': campo,
            'btn_inverso': btn_mais,
            'text_total': text_total,


            'acao': 'subtrair'
        }

        return ft.Row(
            spacing = 0,
            alignment = ft.MainAxisAlignment.CENTER,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,

            data = {
                'servico': servico,
                'preco': valor,
                'campo': campo,
                'menos': btn_menos,
                'mais': btn_mais
            },

            controls = [
                btn_menos,
                campo,
                btn_mais
            ]
        )

    async def pages_dialog(self):
        servicos_inseridos = [] #vem da primeira tela/ validar se há serviço registrado para poder prosseguir
        formas_pagamento = {} #guarda os valores recebidos em cada forma de pagamento
        fields_pagamento = {} #guarda os textfields por keys
        mapa = ['dinheiro/0', 'pix/1', 'cartão/2']
        notificacao = ft.Container(
            top = 0,
            left = 0,
            right = 0,
            bottom = 0,
            expand = True,
            visible = False,
            bgcolor = c.rosa,
            alignment = ft.Alignment.CENTER,
            border_radius = ft.BorderRadius(
                top_left = 34, top_right = 34,
                bottom_left = 0, bottom_right = 0
            ),
        )
        async def refresh_ativos(e):
            campos_ativos = self.lista_options_conclusao.controls[2].controls[0].controls
            for campo_stack in campos_ativos:
                texto_pag = campo_stack.controls[0].data['campo']  # 'Dinheiro', 'Pix' ou 'Cartão'
                await recarregar_valores(e = e, text = texto_pag)
        async def sistema_troco(e = None, update = True):
            total_pago = Decimal('0')
            for formas in formas_pagamento:
                valor = formas_pagamento[formas]
                if valor in ['', ' ', 'None', None]:
                    print('o valor não pode ser convertido')
                    return
                try:
                    total_pago += self.decimal_from_value(formas_pagamento[formas])
                except Exception:
                    print('valor inválido no troco: ', valor)
                    return
            if total_pago > self.totais:
                text_valor_troco.color = c.verde
                text_valor_troco.value = f'R$ {self.decimal_to_texto(total_pago - self.totais)}'
            elif total_pago < self.totais:
                text_valor_troco.color = c.vermelho
                text_valor_troco.value = f'R$ -{self.decimal_to_texto(self.totais - total_pago)}'
            else:
                text_valor_troco.color = c.preto_icons
                text_valor_troco.value = 'R$ 0,00'
            if update == True:
                text_valor_troco.update()
        async def notificacoes_top(e, msg1 = None, msg2 = None, color = c.branco, bgcolor = c.rosa, som = 'som_error.wav'):
            click = None
            if e != None:
                click = e.control.on_click
                e.control.on_click = None
                e.control.opacity = 0.2
                e.control.update()

            self.alertdialog_global.title_padding = 0
            self.alertdialog_global.title.height = 74 + 26
            self.alertdialog_global.title.width = self.page.width - (2 * vg.margin_left)
            self.alertdialog_global.update()
            notificacao.bgcolor = bgcolor
            notificacao.content = ft.Text(
                text_align = ft.TextAlign.CENTER,
                spans = [
                    ft.TextSpan(
                        text = 'Atenção!\n' if msg1 == None else msg1,
                        style = ft.TextStyle(
                            size = 18, color = color,
                            font_family = 'inter', weight = ft.FontWeight.W_600
                        )
                    ),
                    
                    ft.TextSpan(
                        text = 'Selecione itens para prosseguir.' if msg2 == None else msg2,
                        style = ft.TextStyle(
                            size = 16, color = color,
                            font_family = 'inter', weight = ft.FontWeight.W_500
                        )
                    ),
                ]
            )
            notificacao.visible = True
            await play.som[som].play()
            notificacao.update()

            opacidade = 0.2
            for x in range(8):
                if e != None:
                    opacidade += 0.1
                    e.control.opacity = opacidade
                    e.control.update()
                await asyncio.sleep(0.25)

            notificacao.visible = False
            self.alertdialog_global.title.height = 74
            self.alertdialog_global.title.width = self.page.width - ((2 * vg.margin_left) + (2 * self.margin_lateral_interna))
            self.alertdialog_global.title_padding = ft.Padding(
                left = self.margin_lateral_interna,
                right = self.margin_lateral_interna,
                top = 26,
            )
            if e != None:
                e.control.on_click = click
                e.control.opacity = 1
                e.control.update()

            self.alertdialog_global.update()
            notificacao.update()
        async def conversao_campo(e = None, campo = None, text = None, modulo = 0):
            if campo != None:
                valor = str(campo.value).replace(' ', '')
            else:
                valor = self.totais
                valor = str(valor)
                print('deu:', valor)

            if valor in ['', 'None', None]:
                valor = '0,00'
            if ',' not in valor:
                valor = valor.split('.')
                if len(valor) >= 2:
                    if valor[0] == '':
                        valor = '0' + (',' + valor[-1])
                    else:
                        valor = ''.join(valor[:-1]) + (',' + valor[-1])
                else:
                    valor = f'{valor[0]},00'
            elif ',' in valor:
                valor = valor.replace('.', '')
                valor = valor.split(',')
                if len(valor) >= 2:
                    if valor[0] == '':
                        valor = '0' + (',' + valor[-1])
                    else:
                        valor = ''.join(valor[:-1]) + (',' + valor[-1])
                else:
                    valor = f'{valor[0]},00'

            try:
                valor_decimal = self.decimal_from_value(valor)
                if campo != None:
                    print('Converteu pra campo: ', self.totais)
                    campo.value = self.decimal_to_texto(valor_decimal)
                else:
                    if text != None:
                        print('Converteu pra texto: ', self.totais)
                        text.value = self.decimal_to_texto(valor_decimal)

                self.page_conclusao.update()   
                if modulo != 0:             
                    return 'Sucesso'

            except Exception as err:
                await notificacoes_top(
                    e = None,
                    msg1 = 'Ops..!\n',
                    msg2 = 'Valor inválido. (conversão)'
                )

                if campo != None:
                    campo.value = ''
                    await campo.focus()
                
                print('O ERRO FOI', err)
                if modulo != 0:
                    return 'Error'
        async def adicionais_descontos(e = None):
            if e != None:
                if e.control.data['control'] == 'switch':
                    self.porcentagem_ativa = not self.porcentagem_ativa
                coluna = e.control.data['coluna']
            else:
                coluna = self.coluna_main_descontos_adicionais

            campo_1 = coluna.data['campo_1']  # desconto
            campo_2 = coluna.data['campo_2']  # adicional

            await conversao_campo(e = e, campo = campo_1)
            await conversao_campo(e = e, campo = campo_2)

            valor_desconto = self.decimal_from_value(campo_1.value)
            valor_adicional = self.decimal_from_value(campo_2.value)

            base = self.decimal_from_value(self.totais_reserva)

            if self.porcentagem_ativa:
                operacao_desconto = base * (valor_desconto / Decimal('100'))
                operacao_adicional = base * (valor_adicional / Decimal('100'))
                self.descontos_Fn = f'% {operacao_desconto}'
                self.adicionais_Fn = f'% {operacao_desconto}'
            else:
                operacao_desconto = valor_desconto
                operacao_adicional = valor_adicional
                self.descontos_Fn = f'$ {operacao_desconto}'
                self.adicionais_Fn = f'$ {operacao_desconto}'

            self.totais = base - operacao_desconto + operacao_adicional

            await conversao_campo(e, text = text_valor_total)
            await sistema_troco()
            self.alertdialog_global.update()
        async def carregar_page_now(titulo_new):
            self.titulo = titulo_new
            self.alertdialog_global.title = ft.Stack(
                height = 74,
                width = self.page.width - ((2 * vg.margin_left) + (2 * self.margin_lateral_interna)),
                controls = [
                    ft.Row(
                        top = 0,
                        left = 0,
                        right = 0,
                        bottom = 0,
                        alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                        vertical_alignment = ft.CrossAxisAlignment.CENTER,

                        controls = [
                            ft.Text(
                                value = self.titulo,
                                style = ft.TextStyle(size = 22, color = c.preto_icons, font_family = 'inter')
                            ),

                            ft.Container(
                                width = 64,
                                height = 64,
                                border_radius = 24,
                                bgcolor = ft.Colors.TRANSPARENT,
                                alignment = ft.Alignment.CENTER,

                                content = ft.Icon(
                                    icon = ft.CupertinoIcons.XMARK,
                                    size = 24, color = c.preto_icons
                                ),

                                on_click = self.fechar,
                                ink = True
                            )
                        ]
                    ),

                    notificacao
                ]
            )
            self.alertdialog_global.content.height = self.page.height * 3 / 4
            self.alertdialog_global.content.width = self.page.width - 2 * vg.margin_left
        async def return_atendimento(e):
            await asyncio.sleep(0.26)
            self.alertdialog_global.content = self.page_servico
            await carregar_page_now('Atendimento')  
            self.alertdialog_global.update()
        async def go_conclusao(e):
            self.totais_reserva = Decimal('0')
            for totais_value_C in self.servicos_atendimento:
                self.totais_reserva += self.decimal_from_value(self.servicos_atendimento[totais_value_C]['total'])
            if self.totais in [0, None, '']:
                await notificacoes_top(e)
                return
            else:
                self.totais = self.totais_reserva
                notificacao.visible = False
                self.alertdialog_global.content = self.page_conclusao
                await carregar_page_now('Conclusão')
                self.alertdialog_global.update()
                await conversao_campo(e, campo = None, text = text_valor_total)
                text_valor_total.value = f'R$ {text_valor_total.value}'
                nova_coluna = ft.Column(
                    spacing = 0,
                    expand = True,
                    scroll = ft.ScrollMode.AUTO,
                    alignment = ft.MainAxisAlignment.START,
                    horizontal_alignment = ft.CrossAxisAlignment.START,
                    margin = ft.Margin(bottom = 22)
                )
                caminho = self.lista_options_conclusao.controls[0].content
                lista_antiga = caminho.controls[1]
                caminho.controls.remove(lista_antiga)
                for servico in self.servicos_atendimento:
                    servicos_inseridos.append(servico)
                    linha_servico = ft.Column(
                            spacing = 0,
                            height = 64,
                            alignment = ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.START,
                            margin = ft.Margin(left = self.margin_lateral_interna, right = self.margin_lateral_interna),
        
                            controls = [
                                ft.Row(
                                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                                    vertical_alignment = ft.CrossAxisAlignment.CENTER,
        
                                    controls = [
                                        ft.Text(
                                            value = f'{self.servicos_atendimento[servico]['quantidade']}x {servico}',
                                            size = 16, color = c.preto_icons, font_family = 'inter'
                                        ),
                                        ft.Text(
                                            value = f'R$ {self.servicos_atendimento[servico]['total']}',
                                            size = 16, color = c.preto_icons, font_family = 'inter'
                                        ),
                                    ]
                                ),
        
                                ft.Row(
                                    alignment = ft.MainAxisAlignment.START,
                                    vertical_alignment = ft.CrossAxisAlignment.CENTER,
                                    
                                    controls = [
                                        ft.Text(
                                            value = f'Und R$ {self.servicos_atendimento[servico]['valor']}',
                                            size = 16, color = c.sub_textos, font_family = 'inter'
                                        )
                                    ]
                                )
                            ]
                        )
                    nova_coluna.controls.append(linha_servico)
                nova_coluna.controls.append(ft.Row(height = 100))
                caminho.controls.insert(1, nova_coluna)

                campos_ativos = self.lista_options_conclusao.controls[2].controls[0].controls
                for campos_txt in campos_ativos:
                    campos_txt.controls[0].controls[0].value = self.decimal_to_texto(self.totais / Decimal(str(len(campos_ativos))))

                for campo_stack in campos_ativos:
                    await conversao_campo(e = e, campo = campo_stack.controls[0].controls[0])
                    if campo_stack.controls[0].data['campo'].lower() in ['cartao', 'cartão']:
                        self.value_fieldtext_cartao = self.decimal_from_value(campo_stack.controls[0].controls[0].value)
                
                await refresh_ativos(e = e)
                await sistema_troco(e = e, update = False)
                await adicionais_descontos()
                if self.box_cartao_ativo:
                    await converter_credito_debito(card = True)
                self.alertdialog_global.update()
        async def recarregar_valores(e = None, text = None):
            if text != None:
                chave = text.value if type(text) != str else text
                if chave.lower() not in ['cartao', 'cartão']:
                    formas_pagamento[chave] = fields_pagamento[chave].value
                for pag in fields_pagamento:
                    campo_txt = fields_pagamento[pag].data['text']
                    if campo_txt in formas_pagamento and campo_txt.lower() not in ['cartao', 'cartão']: #verifico se o text do pagamento ja foi acionado
                        formas_pagamento[campo_txt] = str(fields_pagamento[pag].value) #atualizo os valores do campo de pagamento
        async def subir_venda(e):
            try:
                await refresh_ativos(e = e)
                if len(formas_pagamento) == 0:
                    await notificacoes_top(
                        e,
                        msg1 = 'Atenção!\n',
                        msg2 = 'Selecione a forma de pagamento.',
                    )
                    return
                    
                total_final = Decimal('0')
                for formas in formas_pagamento:
                    total_final += self.decimal_from_value(formas_pagamento[formas])

                if total_final >= (self.totais - Decimal('0.03')):
                    await notificacoes_top(
                        e,
                        msg1 = 'Sucesso!\n',
                        msg2 = 'Sua venda foi registrada e salva.',
                        bgcolor = c.verde,
                        color = c.branco,
                        som = 'venda_realizada.mp3'
                    )
                    servicos = ''
                    for servico in self.servicos_atendimento:
                        quantidade = self.servicos_atendimento[servico]['quantidade']
                        total_servico = self.servicos_atendimento[servico]['total']
                        if servicos != '':
                            servicos += f'/#servico:{servico} #quantidade:{quantidade} #total:{total_servico}'
                        else:
                            servicos += f'#servico:{servico} #quantidade:{quantidade} #total:{total_servico}'
                    pagamentos_list = {
                        'Pix': 0.00,
                        'Dinheiro': 0.00,
                        'Cartão_crédito': 0.00,
                        'Cartão_débito': 0.00,
                    }

                    for pagamento in pagamentos_list:
                        if pagamento in formas_pagamento:
                            pagamentos_list[pagamento] = formas_pagamento[pagamento]

                    pix = pagamentos_list['Pix']
                    dinheiro = pagamentos_list['Dinheiro']
                    cartao_debito = pagamentos_list['Cartão_débito']
                    cartao_credito = pagamentos_list['Cartão_crédito']
                        
                    bd.registrar_atendimento(
                        servicos = servicos,
                        subtotal = self.totais_reserva,
                        descontos = self.descontos_Fn,
                        adicionais = self.adicionais_Fn,
                        valor_total = self.totais,
                        taxa_operacao = self.taxa_operacao,
                        pix = pix, dinheiro = dinheiro,
                        cartao_credito = cartao_credito,
                        cartao_debito = cartao_debito,
                        troco = total_final - self.totais
                    )
                else:
                    await notificacoes_top(
                        e,
                        msg1 = 'Saldo insuficiente!\n',
                        msg2 = 'O valor recebido é inferior ao total.',
                    )
            except Exception as err:
                print('Erro subir_venda: ', err)
                await notificacoes_top(
                    e,
                    msg1 = 'Ops..!\n',
                    msg2 = 'O valor inserido é inválido.'
                )
        async def recarregar_no_field(e):
            text = e.control.data['text']
            if text.lower() not in ['cartao', 'cartão']:
                formas_pagamento[text] = e.control.value
            await recarregar_valores(e, referencia_p_field[text])
        async def focar_campo(e, focus = False):
            stack = e.control.data['stack']
            field = e.control
            coluna = globals_controls['coluna']

            if focus == False:
                field.label_style = ft.TextStyle(
                    color = c.sub_textos, size = 20,
                    font_family = 'inter'
                )
                stack.controls[1].controls[0].color = c.sub_textos
            else:
                field.label_style = ft.TextStyle(
                    color = c.azul_violeta, size = 20,
                    font_family = 'inter'
                )
                stack.controls[1].controls[0].color = c.lilas_calmo
                await asyncio.sleep(0.3)
                await coluna.scroll_to(
                    scroll_key = field.key,
                    duration = 500,
                    curve = ft.AnimationCurve.EASE_IN_OUT
                )
        async def focar_card(e):
            card = e.control
            coluna = self.lista_options_conclusao

            await asyncio.sleep(0.3)
            await coluna.scroll_to(
                scroll_key = card.key,
                duration = 300,
                curve = ft.AnimationCurve.EASE_IN_OUT
            )
        async def rodar_focus(e):
            await focar_campo(e, focus = True)
        async def rodar_blur(e):
            await focar_campo(e, focus = False)
        async def change_values_campos_CONCLUSAO(e):
            campo = e.control
            devolutiva_de_erro = await conversao_campo(e, campo, modulo = 1)
            await rodar_blur(e)
            await recarregar_no_field(e)
            if devolutiva_de_erro == 'Error':
                return
            anterior[campo] = self.decimal_from_value(campo.value)
            referencia = self.lista_options_conclusao.controls[2].controls[0].controls
            quantiade_controls = len(referencia)
            for fields in referencia: #percorre todos os campos de texto ativos
                if quantiade_controls - len(anterior) > 0:
                    if fields.controls[0].controls[0] not in anterior:
                        calculo = self.decimal_to_texto((self.totais - sum((anterior[x] for x in anterior), Decimal('0'))) / Decimal(str(quantiade_controls - len(anterior))))
                        fields.controls[0].controls[0].value = calculo if '-' not in str(calculo) else fields.controls[0].controls[0].value
                        fields.controls[0].controls[0].update()
                await conversao_campo(e, fields.controls[0].controls[0])

            await refresh_ativos(e = e)
            print(formas_pagamento)
            await sistema_troco(e)
            campo.update()
        async def campos_pagamento_CONCLUSAO(button):
            campo = button.data['campo'] #stack que guarda o campo
            coluna_stack = button.data['coluna_stack']

            encontrado = False
            if len(self.lista_options_conclusao.controls[2].controls[0].controls) > 0:
                for colunas in self.lista_options_conclusao.controls[2].controls[0].controls:
                    if campo in colunas.controls:
                        self.lista_options_conclusao.controls[2].controls[0].controls.remove(colunas)
                        self.lista_options_conclusao.controls[2].controls[0].update()
                        anterior.pop(button.data['field'], None)
                        encontrado = True
                        break

            if not encontrado:
                pagamentos_list = []
                pix_map = {
                    ('dinheiro', 'cartão'): 1,
                    ('dinheiro',): 1,
                    ('cartão',): 0,
                    (): 0,
                }
                for x in  mapa:
                    print('rodou')
                    if x.split('/')[0] == button.data['modalidade'].lower():
                        if x.split('/')[0].lower() == 'pix':
                            for pagamentos in self.lista_options_conclusao.controls[2].controls[0].controls:
                                pagamentos_list.append(pagamentos.controls[0].data['campo'].lower())
                            for posicao in pix_map:
                                if posicao == tuple(pagamentos_list):
                                    x = int(pix_map[posicao])
                        else:
                            x = int(x.split('/')[1])
                        print('stop')
                        break
                print('x:', x)
                print('tipo:', type(x))
                campo.value = ''

                self.lista_options_conclusao.controls[2].controls[0].controls.insert(x, coluna_stack)

            quantidade = len(self.lista_options_conclusao.controls[2].controls[0].controls)
            if quantidade > 0:
                for campos_on in self.lista_options_conclusao.controls[2].controls[0].controls:
                    campos_on.controls[0].controls[0].value = f'{self.totais / quantidade:.2f}'
                    await conversao_campo(campo = campos_on.controls[0].controls[0])
                    if campos_on.controls[0].controls[0].data['text'].lower() in ['cartao', 'cartão']:
                        self.value_fieldtext_cartao = self.decimal_from_value(campos_on.controls[0].controls[0].value)
                        await converter_credito_debito(card = True)

            self.lista_options_conclusao.controls[2].update()
        async def converter_credito_debito(e = None, card = False, campo = False):
            if campo:
                await rodar_blur(e)
                await conversao_campo(e, campo = e.control)
                self.value_fieldtext_cartao = self.decimal_from_value(e.control.value)
            if card == False and campo == False:
                self.cartao_credito = not self.cartao_credito

            if self.cartao_credito:
                cartao = 'Cartão_crédito'
                if 'Cartão_débito' in formas_pagamento:
                    formas_pagamento.pop('Cartão_débito', None)
            else:
                cartao = 'Cartão_débito'
                if 'Cartão_crédito' in formas_pagamento:
                    formas_pagamento.pop('Cartão_crédito', None)

            campo_value_fx = self.value_fieldtext_cartao #valor registrado no momento que o campo perde foco

            if self.cartao_credito:
                taxa = self.taxa_credito_C
            else:
                taxa = self.taxa_debito_C

            self.taxa_cartoes = taxa
            self.taxa_operacao = taxa
            await conversao_campo(e, campo = self.fieldtext_cartao)
            self.fieldtext_cartao.value = self.decimal_to_texto(campo_value_fx + (campo_value_fx * taxa))
            self.value_taxa_cartao = self.decimal_from_value(self.fieldtext_cartao.value)
            await conversao_campo(e, campo = self.fieldtext_cartao)
            if self.box_cartao_ativo:
                formas_pagamento[cartao] = str(self.value_fieldtext_cartao)
                print(formas_pagamento)
            await sistema_troco()
            self.alertdialog_global.update()
        async def campo_cartao(e):
            await change_values_campos_CONCLUSAO(e)
            await converter_credito_debito(e = e, campo = True)
        async def pagamento_select(e):
            button = e.control
            state = button.data['ativo']
            radio = button.data['radio']
            radio_interno = radio.content
            icon = button.content.controls[1].controls[0] #icon do card de pagamento
            text = button.content.controls[1].controls[1] #texto do card de pagamento
            if text.value not in referencia_p_field:
                referencia_p_field[text.value] = text

            if state == False:
                button.data['ativo'] = not button.data['ativo']
                button.border = ft.Border.all(width = 2, color = c.azul_violeta)
                radio.border = ft.Border.all(width = 2, color = c.azul_violeta)
                radio_interno.bgcolor = c.azul_violeta
                icon.color = c.azul_violeta
                text.color = c.azul_violeta
                if button.data['modalidade'].lower() in ['cartão', 'cartao']:
                    self.box_cartao_ativo = True
                    await converter_credito_debito(card = True)
                await campos_pagamento_CONCLUSAO(button = button)
                
                print(f'on {text.value}')
            else:
                button.data['ativo'] = not button.data['ativo']
                button.border = ft.Border.all(width = 0, color = ft.Colors.TRANSPARENT)
                radio.border = ft.Border.all(width = 2, color = c.bordas)
                radio_interno.bgcolor = c.background
                icon.color = c.sub_textos
                text.color = c.sub_textos
                await campos_pagamento_CONCLUSAO(button = button)
                if button.data['modalidade'].lower() in ['cartão', 'cartao']:
                    self.box_cartao_ativo = False
                    self.taxa_operacao = 0
                    await conversao_campo(e, text = text_valor_total)
                    if 'Cartão_crédito'in formas_pagamento:
                        formas_pagamento.pop('Cartão_crédito', None)
                    elif 'Cartão_débito' in formas_pagamento:
                        formas_pagamento.pop('Cartão_débito', None)
                    print('desligou mas ficou:', formas_pagamento)

                formas_pagamento.pop(text.value, None)
                
                print(f'off {text.value}')

            await refresh_ativos(e)
            await sistema_troco(e)
            self.page_conclusao.update()
            print(formas_pagamento)
            
            button.update()
            await focar_card(e)
        async def switch_fields(
            text = None,
            stack = None,
            label_text_1 = None,
            label_text_2 = None,
            campo_switch = False,
            tipo1= None, tipo2 = None,
            icon_1 = None, icon_2 = None,
        ):
            
            switch_e_text = ft.Row(
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment = ft.CrossAxisAlignment.CENTER,
                controls = [
                    ft.Text(
                        value = text,
                        size = 16, color = c.sub_textos,
                        font_family = 'inter',
                        margin = ft.Margin(left = self.margin_lateral_interna)
                    ),

                    ft.CupertinoSwitch(
                        value = True,
                        active_track_color = c.lilas,
                        data = {'control': 'switch'},
                        margin = ft.Margin(right = self.margin_lateral_interna)
                    )
                ]
            )

            if campo_switch == True:
                async def conversoes(e):
                    await rodar_blur(e)
                    await conversao_campo(e, campo = e.control)
                    await adicionais_descontos(e)
                def create(icon, label, tipo):
                    campo = ft.Stack(
                        col = 1,
                        expand = True,
                        margin = ft.Margin(
                            top = vg.margin_top,
                        ),
                        data = {
                            'campo': text,
                        },
                        controls = []
                    )
                    field = ft.TextField(
                        expand = True,
                        key = ft.ScrollKey(f'Key_{text}'),
                        label = label,
                        bgcolor = c.branco,
                        label_style = ft.TextStyle(
                            size = 20, color = c.sub_textos,
                            font_family = 'inter'
                        ),

                        text_style = ft.TextStyle(
                            size = 16, color = c.preto_icons, font_family = 'inter'
                        ),

                        data = {
                            'stack': campo,
                            'tipo': tipo,
                            'control': 'field',
                        },

                        content_padding = ft.Padding(top = 22, left = 50, bottom = 22),
                        keyboard_type = ft.KeyboardType.NUMBER,
                        focused_border_color = c.lilas_calmo,
                        border_color = c.bordas,
                        border_radius = 24,

                        on_focus = rodar_focus,
                        on_blur = conversoes,
                    )
                    coluna = ft.Column(
                        top = 0,
                        left = 14,
                        bottom = 0,
                        alignment = ft.MainAxisAlignment.CENTER,
                        horizontal_alignment = ft.CrossAxisAlignment.START,
                        controls = [
                            ic.svg_icon(
                                icon,
                                size = 30, color = c.sub_textos,
                            )
                            if isinstance(icon, str) else
                            ft.Icon(
                                icon = icon,
                                size = 30, color = c.sub_textos
                            ),
                        ]
                    )
                    campo.controls.extend([field, coluna])
                    return campo  
                coluna_camp = ft.Column(
                    data = {},
                    alignment = ft.MainAxisAlignment.START,
                    horizontal_alignment = ft.CrossAxisAlignment.START,
                    controls = [
                        ft.ResponsiveRow(
                            columns = 2,
                            expand = True,
                            alignment = ft.MainAxisAlignment.START,
                            vertical_alignment = ft.CrossAxisAlignment.CENTER,

                            margin = ft.Margin(
                                left = self.margin_lateral_interna,
                                right = self.margin_lateral_interna
                            ),
                            
                            controls = [
                                create(icon = icon_1, label = label_text_1, tipo = tipo1),
                                create(icon = icon_2, label = label_text_2, tipo = tipo2),
                            ]
                        ),
                        switch_e_text
                    ]
                )
                switch_e_text.controls[1].on_change = adicionais_descontos
                switch_e_text.controls[1].data['coluna'] = coluna_camp
                coluna_camp.data['control'] = 'coluna_main'
                coluna_camp.data['campo_1'] = coluna_camp.controls[0].controls[0].controls[0] #passa a referencia do textfield para o data da coluna
                coluna_camp.data['campo_2'] = coluna_camp.controls[0].controls[1].controls[0] #passa a referencia do textfield para o data da coluna
                coluna_camp.controls[0].controls[0].controls[0].data['coluna'] = coluna_camp  #passa a referencia da coluna pro textfield
                coluna_camp.controls[0].controls[1].controls[0].data['coluna'] = coluna_camp  #passa a referencia da coluna pro textfield
                self.coluna_main_descontos_adicionais = coluna_camp
                return coluna_camp

            else:
                stack.controls.append(switch_e_text)
        async def cards_pagamento_CONCLUSAO(
            icon = 'triangulo_alerta',
            text = 'Vazio', on_blur = None,
            switch = False, text_switch = None,
            top = 0, left = 0, right = 0, bottom = 0,
        ):
            campo = ft.Stack(
                    expand = True,
                    margin = ft.Margin(
                        top = vg.margin_top,
                    ),
                    data = {
                        'campo': text,
                    },
                    controls = []
                )

            field = ft.TextField(
                    expand = True,
                    key = ft.ScrollKey(f'Key_{text}'),
                    label = f'Recebido em {text.lower()}',
                    bgcolor = c.branco,
                    label_style = ft.TextStyle(
                        size = 20, color = c.sub_textos,
                        font_family = 'inter'
                    ),

                    text_style = ft.TextStyle(
                        size = 16, color = c.preto_icons, font_family = 'inter'
                    ),

                    content_padding = ft.Padding(top = 22, left = 50, bottom = 22),
                    keyboard_type = ft.KeyboardType.NUMBER,
                    focused_border_color = c.lilas_calmo,
                    border_color = c.bordas,
                    border_radius = 24,

                    margin = ft.Margin(
                        left = self.margin_lateral_interna,
                        right = self.margin_lateral_interna
                    ),

                    on_focus = rodar_focus,
                    on_blur = change_values_campos_CONCLUSAO if on_blur == None else on_blur,
                )

            coluna = ft.Column(
                    top = 0,
                    left = 38,
                    bottom = 0,
                    alignment = ft.MainAxisAlignment.CENTER,
                    horizontal_alignment = ft.CrossAxisAlignment.START,
                    controls = [
                        ic.svg_icon(
                            icon,
                            size = 30, color = c.sub_textos,
                        )
                        if isinstance(icon, str) else
                        ft.Icon(
                            icon = icon,
                            size = 30, color = c.sub_textos
                        ),
                    ]
                )

            campo.controls.extend([field, coluna])
            field.data = {'stack': campo, 'text': text}
            fields_pagamento[text] = field #Todos os field são adicionados ao dicionariio no momento da sua criação

            coluna_stack = ft.Column(
                alignment = ft.MainAxisAlignment.START,
                horizontal_alignment = ft.CrossAxisAlignment.START,
                controls = [
                    campo
                ]
            )

            if switch == True:
                await switch_fields(
                    text = text_switch,
                    stack = coluna_stack,
                )
                
                coluna_stack.controls[1].controls[1].on_change = converter_credito_debito
                self.fieldtext_cartao = field
            
            radio = ft.Container(
                top = 12,
                left = 12,
                width = 30,
                height = 30,
                border_radius = 15,
                bgcolor = c.background,
                alignment = ft.Alignment.CENTER,
                border = ft.Border.all(width = 2, color = c.bordas),

                content = ft.Container(
                    width = 20,
                    height = 20,
                    border_radius = 10,
                    bgcolor = c.background
                )
            )

            card = ft.Container(
                col = 1,
                height = 180,
                bgcolor = c.branco,
                border_radius = 24,
                shadow = c.shadow_leve(),
                on_click = pagamento_select,
                key = ft.ScrollKey(f'Key_{text}_card'),
                ink = True,

                width = (
                    self.page.width - (
                        ((2 * vg.margin_left) + (2 * self.margin_lateral_interna) + (2 * 12))
                    )
                ) / 3,

                # ^ DEVOLVE A LARGURA TOTAL DISPONÍVEL DA TELA DESCONTANDO AS MARGINS E SPAÇOS,
                # ^ DIVIDE-OS PELA QUANTIDADE DE BOTÕES E SE OBTEM UMA LARGURA IGUAL PARA TODOS

                data = {
                    'radio': radio,
                    'ativo': False,
                    'modalidade': text,
                    'coluna_stack': coluna_stack,
                    'field': field,
                    'campo': campo
                },

                margin = ft.Margin(
                    top = top,
                    left = left,
                    right = right,
                    bottom = bottom
                ),
                
                content = ft.Stack(
                    height = 140,
                    alignment = ft.Alignment.CENTER,
                    
                    controls = [
                        radio,
                                
                        ft.Column(
                            top = 45,
                            bottom = 35,
                            height = 70,
                            alignment = ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER,

                            controls = [
                                ic.svg_icon(
                                    icon,
                                    size = 30, color = c.sub_textos,
                                )

                                if isinstance(icon, str) else

                                ft.Icon(
                                    icon = icon,
                                    size = 30, color = c.sub_textos
                                ),
                                
                                ft.Text(
                                    value = text,
                                    size = 16, color = c.sub_textos,
                                    font_family = 'inter',
                                ),
                            ]
                        ),
                    ]
                )

                # ^ CAMINHO PARA ICON: e.control.content.controls[1].controls[0]
                # ^ CAMINHO PARA TEXT: e.control.content.controls[1].controls[1]
                # ^ CAMINHO PARA RADIO: e.control.content.controls[0]
                # ^ CAMINHO PARA RADIO_INTERNO: e.control.content.controls[0].content
            )

            return card
        async def atualizar_nome_cliente_CONCLUSAO(e):
            edit = e.control
            ativo = edit.data['ativo']
            caminho = self.lista_options_conclusao.controls[0].content.controls[0].controls[0]

            if campo_cliente.value not in ['', 'None', None]:
                text_cliente.value = campo_cliente.value

            if ativo == False:
                caminho.controls.remove(text_cliente)
                caminho.controls.insert(0, campo_cliente)
                edit.content = ic.svg_icon(
                    'check_square',
                    size = 35, color = c.preto_icons
                )

                caminho.update()

                if campo_cliente in caminho.controls:
                    await campo_cliente.focus()
            else:
                caminho.controls.remove(campo_cliente)
                caminho.controls.insert(0, text_cliente)
                edit.content = ic.svg_icon(
                    'editar',
                    size = 35, color = c.preto_icons
                )

            edit.data['ativo'] = not edit.data['ativo']
            edit.update()
            caminho.update()

        campo_cliente = ft.TextField(
            expand = True,
            text_style = ft.TextStyle(
                size = 22, color = c.preto_icons,
                font_family = 'inter'
            ),
            hint_text = 'Nome do cliente..',
            hint_style = ft.TextStyle(
                size = 22, color = c.preto_icons,
                font_family = 'inter'
            ),
            border_color = ft.Colors.TRANSPARENT,
            focused_border_color = ft.Colors.TRANSPARENT,
            content_padding = ft.Padding(left = self.margin_lateral_interna)
        )
        text_cliente = ft.Text(
            value = 'Cliente ##',
            size = 22, color = c.preto_icons,
            font_family = 'inter',
            margin = ft.Margin(left = self.margin_lateral_interna)
        )                                     
        anterior = {}
        globals_controls = {'coluna': None}
        referencia_p_field = {}

        self.lista_options_conclusao = ft.Column(
            spacing = 0,
            expand = True,
            scroll = ft.ScrollMode.AUTO,
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,

            controls = [
                ft.Container(
                    expand = True,
                    bgcolor = c.branco,
                    border_radius = 26,
                    shadow = c.shadow_leve(),
                    alignment = ft.Alignment.CENTER,
                    height = self.page.height * 0.4,
                    margin = ft.Margin(
                        top = vg.margin_top,
                        left = self.margin_lateral_interna,
                        right = self.margin_lateral_interna
                    ),

                    content = ft.Column(
                        spacing = 0,
                        expand = True,
                        alignment = ft.MainAxisAlignment.START,
                        horizontal_alignment = ft.CrossAxisAlignment.START,

                        controls = [
                            ft.Column(
                                spacing = 0,
                                alignment = ft.MainAxisAlignment.START,
                                horizontal_alignment = ft.CrossAxisAlignment.START,
                                margin = ft.Margin(
                                    top = self.margin_lateral_interna / 2,
                                    bottom = self.margin_lateral_interna / 2,
                                ),

                                controls = [
                                    ft.Row(
                                        height = 64,
                                        alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                                        vertical_alignment = ft.CrossAxisAlignment.CENTER,
                                        controls = [
                                            ft.Text(
                                                value = 'Cliente ##',
                                                size = 22, color = c.preto_icons,
                                                font_family = 'inter',
                                                margin = ft.Margin(left = self.margin_lateral_interna)
                                            ),

                                            ft.Container(
                                                width = 64,
                                                height = 64,
                                                alignment = ft.Alignment.CENTER,
                                                bgcolor = ft.Colors.TRANSPARENT,
                                                data = {
                                                    'ativo': False,
                                                    'campo': campo_cliente,
                                                    'text': text_cliente,
                                                },
                                                content = ic.svg_icon(
                                                    'editar',
                                                    size = 35, color = c.preto_icons
                                                ),
                                                on_click = atualizar_nome_cliente_CONCLUSAO
                                            )
                                        ]
                                    )
                                ]
                            ),

                            ft.Column(
                                spacing = 0,
                                expand = True,
                                scroll = ft.ScrollMode.AUTO,
                                alignment = ft.MainAxisAlignment.START,
                                horizontal_alignment = ft.CrossAxisAlignment.START
                            ),

                            ft.ResponsiveRow(
                                spacing = 0,
                                columns = 2,
                                alignment = ft.MainAxisAlignment.START,
                                vertical_alignment = ft.CrossAxisAlignment.CENTER,
                                controls = [
                                    ft.Column(
                                        col = 1,
                                        spacing = 0,
                                        alignment = ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment = ft.CrossAxisAlignment.START,
                                        margin = ft.Margin(
                                            left = self.margin_lateral_interna,
                                            bottom = 16
                                        ),

                                        controls = [
                                            ft.Text(
                                                value = 'Total:', expand = True, overflow = ft.TextOverflow.ELLIPSIS,
                                                size = 16, color = c.sub_textos, font_family = 'inter', max_lines = 1
                                            ),

                                            ft.Text(
                                                value = f'R$ 0,00', expand = True, overflow = ft.TextOverflow.ELLIPSIS,
                                                size = 22, color = c.preto_icons, font_family = 'inter', max_lines = 1,
                                                weight = ft.FontWeight.W_500
                                            )
                                        ]
                                    ),
                                    
                                    ft.Column(
                                        col = 1,
                                        spacing = 0,
                                        alignment = ft.MainAxisAlignment.CENTER,
                                        horizontal_alignment = ft.CrossAxisAlignment.START,
                                        margin = ft.Margin(
                                            left = self.margin_lateral_interna,
                                            bottom = 16
                                        ),

                                        controls = [
                                            ft.Text(
                                                value = 'Troco:', expand = True, overflow = ft.TextOverflow.ELLIPSIS,
                                                size = 16, color = c.sub_textos, font_family = 'inter', max_lines = 1
                                            ),

                                            ft.Text(
                                                value = f'R$ 0,00', expand = True, overflow = ft.TextOverflow.ELLIPSIS,
                                                size = 22, color = c.preto_icons, font_family = 'inter', max_lines = 1,
                                                weight = ft.FontWeight.W_500
                                            )
                                        ]
                                    )
                                ]
                            )
                        ]                        
                    )
                ),

                ft.Row(
                    spacing = 12,
                    expand = True,
                    alignment = ft.MainAxisAlignment.START,
                    vertical_alignment = ft.CrossAxisAlignment.CENTER,

                    controls = [
                        await cards_pagamento_CONCLUSAO(
                            icon = 'dinheiro', text = 'Dinheiro',
                            top = vg.margin_top,
                            left = self.margin_lateral_interna,
                        ),

                        await cards_pagamento_CONCLUSAO(
                            icon = ft.Icons.PIX, text = 'Pix',
                            top = vg.margin_top,
                        ),

                        await cards_pagamento_CONCLUSAO(
                            icon = 'cartao', text = 'Cartão',
                            top = vg.margin_top,
                            right = self.margin_lateral_interna,
                            switch = True, text_switch = 'Cartão de crédito',
                            on_blur = campo_cartao
                        ),
                    ]
                ),

                ft.Column(
                    expand = True,
                    alignment = ft.MainAxisAlignment.START,
                    horizontal_alignment = ft.CrossAxisAlignment.START,

                    controls = [
                        ft.Column(
                            spacing = 0,
                            expand = True,
                            alignment = ft.MainAxisAlignment.START,
                            horizontal_alignment = ft.CrossAxisAlignment.START,
                        ),

                        ft.Column(
                            spacing = 0,
                            expand = True,
                            alignment = ft.MainAxisAlignment.START,
                            horizontal_alignment = ft.CrossAxisAlignment.START,

                            controls = [
                                ft.Container(
                                    height = 1.2,
                                    expand = True,
                                    bgcolor = c.bordas,
                                    margin = ft.Margin(
                                        left = self.margin_lateral_interna,
                                        right = self.margin_lateral_interna,
                                        bottom = 8, top = 15
                                    )
                                ),
                                await switch_fields(
                                    label_text_1 = 'Desconto',
                                    label_text_2 = 'Adicional',
                                    icon_1 = 'descontos',
                                    icon_2 = 'adicionais',
                                    text = 'Valor em porcentagem %',
                                    campo_switch = True,
                                    tipo1 = 'Desconto',
                                    tipo2 = 'Adicional'
                                )
                            ]
                        ),
                        ft.Column(height = 70)
                    ]
                )
            ]
        
        )                  
        self.barra_inferior_conclusao = ft.Container(
            height = 110,
            bgcolor = c.branco,
            shadow = c.shadow_leve(x = 0, y = -4),

            border_radius = ft.BorderRadius(
                top_left = 0,
                top_right = 0,
                bottom_left = 34,
                bottom_right = 34
            ),

            content = ft.Row(
                expand = True,
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment = ft.CrossAxisAlignment.CENTER,
        
                controls = [
                    ft.Container(
                        height = 58,
                        bgcolor = c.branco,
                        shadow = c.shadow_leve(y = 2, opc = 0.4),

                        margin = ft.Margin(
                            left = self.margin_lateral_interna,
                        ),
                                        
                        border_radius = 24,
                        alignment = ft.Alignment.CENTER,
        
                        content = ft.Row(
                            spacing = 6,
                            alignment = ft.MainAxisAlignment.CENTER,
                            vertical_alignment = ft.CrossAxisAlignment.CENTER,
                            
                            margin = ft.Margin(left = 26, right = 36),

                            controls = [
                                ic.svg_icon(
                                    'seta_exit',
                                    size = 26, color = c.rosa
                                ),
                                        
                                ft.Text(
                                    value = 'Voltar',
                                    style = ft.TextStyle(
                                        size = 16, color = c.rosa, font_family = 'inter',
                                    ),
                                )
                            ]
                        ),

                        on_click = return_atendimento,
                        ink = True
                    ),

                    ft.Container(
                        height = 58,
                        shadow = c.shadow_buttons(),

                        gradient = c.gradiente_top_bottom(c.gradiente_botoes),
                        margin = ft.Margin(
                            right = self.margin_lateral_interna,
                        ),
                                        
                        border_radius = 24,
                        alignment = ft.Alignment.CENTER,
        
                        content = ft.Text(
                            value = 'Finalizar',
                            style = ft.TextStyle(
                                size = 16, color = c.branco, font_family = 'inter',
                            ),
                            margin = ft.Margin(left = 36, right = 36)
                        ),

                        on_click = subir_venda,
                        ink = True
                    )
                ]
            )
        )
        self.page_conclusao = ft.Column(
                spacing = 0,
                expand = True,
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                controls = [
                    ft.Column(
                        expand = True,
                        alignment = ft.MainAxisAlignment.START,
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                        controls = [
                            self.lista_options_conclusao,
                        ]
                    ),

                    self.barra_inferior_conclusao,
                ]
            )

        text_valor_total = self.lista_options_conclusao.controls[0].content.controls[2].controls[0].controls[1]
        text_valor_troco = self.lista_options_conclusao.controls[0].content.controls[2].controls[1].controls[1]
        globals_controls['coluna'] = self.lista_options_conclusao

        self.tags_sugestoes = ft.Row(
                margin = ft.Margin(top = 6),
                scroll = ft.ScrollMode.AUTO,
                alignment = ft.MainAxisAlignment.START,
                vertical_alignment = ft.CrossAxisAlignment.CENTER,

                controls = []
            )
        self.lista_options = ft.Column(
                spacing = 0,
                expand = True,
                scroll = ft.ScrollMode.AUTO,

                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,

                controls = [ft.ProgressRing(color = c.lilas_calmo, height = 100, width = 100)]
            )      
        self.barra_inferior = ft.Container(
                height = 110,
                bgcolor = c.branco,
                shadow = c.shadow_leve(x = 0, y = -4),

                border_radius = ft.BorderRadius(
                    top_left = 0,
                    top_right = 0,
                    bottom_left = 34,
                    bottom_right = 34
                ),

                content = ft.Row(
                    expand = True,
                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment = ft.CrossAxisAlignment.CENTER,
            
                    controls = [
                        ft.Column(
                            spacing = 0,
                            alignment = ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.START,
            
                            controls = [
                                ft.Text(
                                    value = 'Subtotal', margin = ft.Margin(left = self.margin_lateral_interna),
                                    style = ft.TextStyle(size = 14, color = c.sub_textos, font_family = 'inter')
                                ),
            
                                ft.Text(
                                    value = 'R$ 0,00', margin = ft.Margin(left = self.margin_lateral_interna),
                                    style = ft.TextStyle(size = 22, color = c.preto_icons, font_family = 'inter')
                                ),
                                
                                ft.Row(height = 6),
                            ]
                        ),
            
                        ft.Container(
                            height = 58,
                            shadow = c.shadow_buttons(),
                            gradient = c.gradiente_top_bottom(c.gradiente_botoes),

                            margin = ft.Margin(
                                right = self.margin_lateral_interna,
                            ),
                                            
                            border_radius = 24,
                            alignment = ft.Alignment.CENTER,
            
                            content = ft.Text(
                                value = 'Prosseguir',
                                style = ft.TextStyle(
                                    size = 16, color = c.branco, font_family = 'inter',
                                ),

                                margin = ft.Margin(left = 26, right = 26)
                            ),

                            on_click = go_conclusao,
                            ink = True
                        )
                    ]
                )
            )
        self.page_servico = ft.Column(
            spacing = 0,
            expand = True,
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                ft.Column(
                    expand = True,
                    alignment = ft.MainAxisAlignment.START,
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                    controls = [
                        self.barra_pesquisa(
                            on_focus = self.pesquisa_servicos,
                            on_change = self.pesquisa_servicos
                        ),

                        self.tags_sugestoes,
                        self.lista_options,
                    ]
                ),

                self.barra_inferior,
            ]
        )

        self.alertdialog_global.content = self.page_servico
        self.alertdialog_global.data = {
            'tags_atendimento': self.tags_sugestoes,
            'lista_atendimento': self.lista_options,
            'barra_inferior_atendimento': self.barra_inferior,
            'barra_pesquisa_atendimento': self.barra_pesquisa,
            
            # 'tags_conclusao': self.tags_sugestoes,
            'lista_conclusao': self.lista_options_conclusao,
            'barra_inferior_conclusao': self.barra_inferior_conclusao,
            'barra_pesquisa_conclusao': self.barra_pesquisa,
        }

        await carregar_page_now('Atendimento')