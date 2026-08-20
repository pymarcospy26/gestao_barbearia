import asyncio
import flet as ft
import icons as ic
import banco as bd
import colors as c

import play_audio as play
import conversores as conv
import variaveis_globais as vg
import dicionario_idioma as dic

from frontend.pages import tela_pagamento_atendimento as pag

class Tela_Atendimento:
    def __init__(self, page: ft.Page):
        vg.totais = 0
        self.page = page
        vg.armazenamento_totais_p_servico.clear()

        self.pagamentos_criados = []
        self.controls_servicos_carregados = {}
        self.servicos_carregados = vg.servicos_carregados #DADOS DE TODOS OS DADOS CARREGADOS DO BANCO BD
        self.lista_scroll = ft.Column(
            spacing = 0,
            expand = True,
            scroll = ft.ScrollMode.AUTO,
            alignment = ft.MainAxisAlignment.START,
            margin = ft.Margin(top = 8, bottom = 8),
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        )

        self.lista_tags = []
        self.space_tags = ft.Row(
            wrap = True,
            width = self.page.width - (2 * 26),
            alignment = ft.MainAxisAlignment.START,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,
            controls = self.lista_tags
        )

    async def go_pagamento(self, e):
        async def retorno(e):
            vg.go_pagamento_aprovd = False
            vg.pagina_ativa_go = vg.pagina_atendimento_go

            vg.btn_centro.on_click = vg.nova_tela_atendimento
            vg.btn_centro.content = ic.svg_icon(
                icon = 'vassoura', size = 34, color = c.fundo_neutralo
            )

            await vg.troca_de_pagina(
                e, pagina = vg.pagina_atendimento_go,
                titulo = 'atendimento', icon_config = 'menu',
                preservar_anterior = True
            )

        vg.btn_centro.on_click = retorno
        
        vg.btn_centro.content = ic.svg_icon(
            icon = 'seta_exit', size = 34, color = c.fundo_neutralo
        )

        if vg.go_pagamento_aprovd == False:
            vg.go_pagamento_aprovd = True
            if vg.pagina_pagamento_go == None:
                vg.pagina_pagamento_go = pag.Pagamento(self.page).tela()
                
            vg.pagina_ativa_go = vg.pagina_pagamento_go

            await vg.troca_de_pagina(
                e, pagina = vg.pagina_pagamento_go,
                titulo = 'pagamento', icon_config = 'menu',
                preservar_anterior = True, clear = False
            )

    def recarregar_produtos(self, e, tag):
        if tag in self.servicos_carregados:
            self.lista_scroll.controls.clear()
            for x in self.servicos_carregados[tag]:
                item_filtrado = self.controls_servicos_carregados[self.servicos_carregados['todos'][x]['produto']]
                self.lista_scroll.controls.append(item_filtrado)

        self.fechar_PopUp(e)
        self.page.update()
        
    def abrir_PopUp(self, e):
        vg.box_PopUp.controls[1].content = None
        for x in vg.servicos_carregados:
            tag = ft.Container(
                height = 74,
                border_radius = 28,
                alignment = ft.Alignment.CENTER,
                padding = ft.Padding(left = 12, right = 12),
                border = ft.Border.all(width = 0.6, color = c.texto_suave),

                content = ft.Text(
                    value = x, size = 16, color = c.texto_suave,
                    font_family = 'inter'
                ),

                data = {'tag': x},

                ink = True,
                on_click = lambda e, x = x: self.recarregar_produtos(e, tag = x)
            )

            self.page.update()

            tag.width = tag.width
            self.lista_tags.append(tag)
            
            self.page.update()
        vg.conteudo_box_PopUp(self.page, conteudo = self.space_tags)
        vg.box_PopUp.visible = True
        self.page.update()

    def fechar_PopUp(self, e):
        self.lista_tags.clear()
        self.space_tags.controls.clear()
        vg.box_PopUp.visible = False
        vg.box_PopUp.controls[1].content = None
        self.page.update()

    def decimal(self, valor = None, text_yn = False):
        return conv.Moedas().decimal_n(valor = valor, p_texto = text_yn)

    def conversor(self, valor = None, decimal = None, text_yn = False, cifrao = False):
        return conv.Moedas().conversao_moeda(valor = valor, p_decimal = decimal, p_text = text_yn, cifrao = cifrao)

    def box_servicos(
        self,
        setor = 'setor do servico',
        servico = 'nome do servico',
        valor = 'valor unitario do servico',
        lista: ft.Control = None,
        botao_presseguir = None,
        text_subtotal = None
    ):
        
        lock_quantidade = asyncio.Lock()

        async def acao_botoes_quantidae(e):
            btn_click = e.control
            id_quantidade = btn_click.data['campo']
            btn_mais = btn_click.data['botao_mais']
            btn_menos = btn_click.data['botao_menos']
            box_clik = btn_click.data['box']

            async with lock_quantidade:
                if btn_click.data['x'] == 'menos':
                    if int(id_quantidade.value) > 0:
                        id_quantidade.value = str(int(id_quantidade.value) - 1)

                        if int(id_quantidade.value) == 0:
                            btn_click.on_click = None
                            
                            btn_mais.shadow = None
                            btn_mais.bgcolor = c.fundo_alternativo
                            btn_mais.content.color = c.texto_principal

                            btn_click.opacity = 0.2
                            btn_click.ink = False

                if btn_click.data['x'] == 'mais':
                    id_quantidade.value = str(int(id_quantidade.value) + 1)

                    if int(id_quantidade.value) > 0:
                        btn_click.bgcolor = c.cor_principal_escura
                        btn_click.shadow = c.shadow_leve(opc = 0.56)
                        btn_click.content.color = c.fundo_neutralo

                        btn_menos.on_click = acao_botoes_quantidae
                        btn_menos.opacity = 1
                        btn_menos.ink = True

                        box_clik.animate_opacity = ft.Animation(duration = 0)
                        box_clik.animate_offset = ft.Animation(duration = 0)
                        box_clik.opacity = 0
                        box_clik.offset = ft.Offset(0, -0.26)
                        box_clik.update()

                        await asyncio.sleep(0.02)

                        box_clik.animate_opacity = ft.Animation(
                            curve = ft.AnimationCurve.EASE_IN_OUT,
                            duration = 240
                        )

                        box_clik.animate_offset = ft.Animation(
                            curve = ft.AnimationCurve.EASE_IN_OUT,
                            duration = 240
                        )
                        box_clik.update()

                        box_clik.opacity = 1
                        box_clik.offset = ft.Offset(0, 0)
                        box_clik.update()

            if servico not in vg.armazenamento_totais_p_servico:
                vg.armazenamento_totais_p_servico[servico] = 0

            vg.armazenamento_totais_p_servico[servico] = self.decimal(valor = id_quantidade.value) * self.decimal(valor = valor)
            vg.totais = self.decimal(valor = 0)
            for x in vg.armazenamento_totais_p_servico:
                vg.totais += self.decimal(valor = vg.armazenamento_totais_p_servico[x])

            vg.totais = self.decimal(valor = vg.totais, text_yn = True)

            text_subtotal.value = self.conversor(valor = vg.totais, text_yn = True)
            vg.subtotal = self.conversor(decimal = text_subtotal.value, text_yn = True)
            print(vg.subtotal)

            if self.decimal(valor = vg.totais) >= 1:
                botao_presseguir.bgcolor = None
                botao_presseguir.gradient = c.gradiente_top_bottom(colors = c.gradiente_botoes)
                botao_presseguir.border = ft.Border.all(width = 0, color = ft.Colors.TRANSPARENT)
                botao_presseguir.content.weight = ft.FontWeight.W_600
                botao_presseguir.content.color = c.fundo_neutralo if c.tema == 'claro' else c.fundo
                botao_presseguir.on_click = self.go_pagamento

            else:
                botao_presseguir.bgcolor = c.fundo
                botao_presseguir.gradient = None
                botao_presseguir.border = ft.Border.all(width = 0.6, color = c.texto_suave)
                botao_presseguir.content.weight = ft.FontWeight.NORMAL
                botao_presseguir.content.color = c.texto_suave
                botao_presseguir.on_click = None

            self.page.update()

        campo = ft.Text(
            value = 0, width = 30,
            size = 16, color = c.texto_principal, text_align = ft.TextAlign.CENTER,
            font_family = 'inter', margin = ft.Margin(left = 8, right = 8)
        )

        botao_menos = ft.Container(
            data = {},
            width = 56,
            height = 56,
            opacity = 0.2,
            border_radius = 24,
            shadow = c.shadow_leve(opc = 0.56),
            bgcolor = c.fundo_neutralo,
            alignment = ft.Alignment.CENTER,

            content = ft.Icon(
                icon = ft.CupertinoIcons.MINUS,
                size = 24, color = c.texto_principal,
            ),

            ink = False,
            on_click = acao_botoes_quantidae
        )

        botao_mais = ft.Container(
            data = {},
            width = 56,
            height = 56,
            border_radius = 24,
            bgcolor = c.fundo_alternativo,
            alignment = ft.Alignment.CENTER,
            margin = ft.Margin(right = 26),

            content = ft.Icon(
                icon = ft.CupertinoIcons.PLUS,
                size = 24, color = c.texto_principal,
            ),

            ink = True,
            on_click = acao_botoes_quantidae
        )

        control_quantidade = ft.Row(
            data = {},
            spacing = 8,
            alignment = ft.MainAxisAlignment.CENTER,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,

            controls = [
                botao_menos,
                campo,
                botao_mais,
            ]
        )

        control_quantidade.data = {
            'campo': campo,
            'botao_mais': botao_mais,
            'botao_menos': botao_menos,
            'control_quantidade': control_quantidade,
        }

        box = ft.Container(
            height = 86,
            expand = True,
            key = ft.ScrollKey(f'Key_{setor}/{servico}/{valor}'),
            shadow = c.shadow_leve(),
            bgcolor = c.fundo_neutralo,
            data = {'setor': setor},

            content = ft.Row(
                spacing = 0,
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment = ft.CrossAxisAlignment.CENTER,

                controls = [
                    ft.Column(
                        spacing = 0,
                        margin = ft.Margin(left = 26),
                        alignment = ft.MainAxisAlignment.CENTER,
                        horizontal_alignment = ft.CrossAxisAlignment.START,

                        controls = [
                            ft.Text(
                                value = servico,
                                size = 16, color = c.texto_principal,
                                font_family = 'inter'
                            ),

                            ft.Text(
                                value = valor,
                                size = 14, color = c.texto_secundario,
                                font_family = 'inter'
                            )
                        ]
                    ),

                    control_quantidade
                ]
            ),

            animate_opacity = ft.Animation(
                curve = ft.AnimationCurve.EASE_IN_OUT,
                duration = 240
            ),

            animate_offset = ft.Animation(
                curve = ft.AnimationCurve.EASE_IN_OUT,
                duration = 240
            )
        )

        botao_mais.data = {
            'x': 'mais',
            'campo': campo,
            'botao_mais': botao_mais,
            'botao_menos': botao_menos,
            'control_quantidade': control_quantidade,
            'box': box, 'lista': lista, 'key': box.key, 'subiu': False
        }
        
        botao_menos.data = {
            'x': 'menos',
            'campo': campo,
            'botao_mais': botao_mais,
            'botao_menos': botao_menos,
            'control_quantidade': control_quantidade,
            'box': box, 'lista': lista, 'key': box.key, 'subiu': False
        }
        
        return box

    def tela(self):
        return self.lista()

    def lista(self):
        btn_filtro = ft.Container(
            width = 74,
            height = 74,
            border_radius = 28,
            shadow = c.shadow_leve(),
            alignment = ft.Alignment.CENTER,
            bgcolor = c.cor_principal_escura,
            margin = ft.Margin(right = vg.margin_right),

            content = ic.svg_icon(
                'filtro',
                size = 30, color = c.fundo_neutralo
            ),

            ink = True,
            on_click = self.abrir_PopUp,
        )
        vg.box_PopUp.controls[0].on_click = self.fechar_PopUp

        lista = ft.Column(
            spacing = 16,
            expand = True,
            margin = ft.Margin(top = vg.margin_top),
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.START,

            controls = [
                ft.Row(
                    spacing = 16,
                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment = ft.CrossAxisAlignment.START,
                    controls = []
                )
            ]
        )

        box_lista = ft.Container(
            expand = True,
            border_radius = 28,
            margin = ft.Margin(left = vg.margin_left, right = vg.margin_right),
            shadow = c.shadow_leve(),
            bgcolor = c.fundo_neutralo,
            alignment = ft.Alignment.CENTER,
            content = self.lista_scroll,
            height = self.page.height * 0.44,
        )

        titulo_subtotal = ft.Text(
            value = dic.palavras[dic.idioma_select]['atendimento']['subtotal'],
            size = 16, color = c.texto_secundario, font_family = 'inter'
        )

        texto_subtotal = ft.Text(
            value = vg.moedas_format[vg.moeda_ativa][0],
            size = 32, color = c.texto_principal, font_family = 'inter'
        )

        cifrao = ft.Text(
            value = vg.moedas_format[vg.moeda_ativa][5],
            size = 32, color = c.texto_principal, font_family = 'inter'
        )

        subtotal_completo = ft.Column(
            spacing = 0,
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.START,
            margin = ft.Margin(left = vg.margin_left)
        )

        row_money_format = ft.Row(
            spacing = 4,
            alignment = ft.MainAxisAlignment.START,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,
            controls = []
        )

        if vg.moedas_format[vg.moeda_ativa][4] == -1:
            row_money_format.controls.extend([texto_subtotal, cifrao])

        else:
            row_money_format.controls.extend([cifrao, texto_subtotal])

        subtotal_completo.controls.extend([titulo_subtotal, row_money_format])

        btn_prosseguir = ft.Container(
            height = 74,
            expand = True,
            bgcolor = c.fundo,
            border_radius = 28,
            shadow = c.shadow_leve(),
            alignment = ft.Alignment.CENTER,
            border = ft.Border.all(width = 0.6, color = c.texto_suave),
            margin = ft.Margin(left = vg.margin_left, right = vg.margin_right),
            
            content = ft.Text(
                value = dic.palavras[dic.idioma_select]['atendimento']['prosseguir'],
                size = 16, color = c.texto_suave, font_family = 'inter',
                weight = ft.FontWeight.NORMAL
            ),

            ink = True,
            on_click = None,
        )

        for x in self.servicos_carregados['todos']:
            control_box = self.box_servicos(
                setor = self.servicos_carregados['todos'][x]['setor'],
                valor = self.servicos_carregados['todos'][x]['valor'],
                servico = self.servicos_carregados['todos'][x]['produto'],
                lista = self.lista_scroll, text_subtotal = texto_subtotal,
                botao_presseguir = btn_prosseguir
            )

            self.lista_scroll.controls.append(control_box)
            self.controls_servicos_carregados[self.servicos_carregados['todos'][x]['produto']] = control_box

        lista.controls[0].controls.extend([
            vg.barra_pesquisa(
                text_interno = dic.palavras[dic.idioma_select]['atendimento']['busca_rapida'],
                on_change = lambda e: vg.sistema_de_busca(e, self.page, self.lista_scroll, self.controls_servicos_carregados)
            ),

            btn_filtro
        ])
        lista.controls.append(box_lista)
        lista.controls.append(subtotal_completo)
        lista.controls.append(btn_prosseguir)
        lista.controls.append(ft.Column(height = 360))

        return lista
















