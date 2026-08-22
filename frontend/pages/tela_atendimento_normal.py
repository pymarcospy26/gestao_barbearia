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
        self.lista_scroll = ft.Column(
            spacing = 0,
            expand = True,
            scroll = ft.ScrollMode.AUTO,
            alignment = ft.MainAxisAlignment.START,
            margin = ft.Margin(top = 8, bottom = 8),
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        )

        self.lista_tags = []
        self.lista_tags_ativas = []

        for x in vg.servicos_carregados:
            title_tag = ft.Text(
                value = x, size = vg.size_letra_normal, color = c.texto_suave,
                font_family = 'inter'
            )

            tag = ft.Container(
                opacity = 0.64,
                height = vg.size_botoes * 5 / 6,
                border_radius = vg.raio_borda,
                bgcolor = c.fundo_neutralo,
                width = self.width_tag(texto = x),
                padding = ft.Padding(left = 20, right = 20),
                border = ft.Border.all(width = 0.8, color = c.texto_suave),

                content = ft.Row(
                    alignment = ft.MainAxisAlignment.CENTER,
                    vertical_alignment = ft.CrossAxisAlignment.CENTER,
                    controls = [title_tag]
                ),

                data = {'tag': x, 'ativo': False},

                ink = True,
                on_click = self.selecao_tags
            )
            
            self.page.update()

            self.lista_tags.append(tag)

            if x == vg.todos_txt:
                self.box_ativo(ativar = True, box = tag, update = False)
            
            self.page.update()

        self.space_tags = ft.Row(
            wrap = True,
            spacing = 16,
            run_spacing = 16,
            alignment = ft.MainAxisAlignment.START,
            vertical_alignment = ft.CrossAxisAlignment.START,
            margin = ft.Margin(
                left = vg.margin_left,
                right = vg.margin_right
            )
        )
        self.titulo_tags = ft.Row(
            height = 54,
            alignment = ft.MainAxisAlignment.CENTER,
            vertical_alignment = ft.CrossAxisAlignment.END,
            controls = [
                ft.Text(
                    value = dic.palavras[dic.idioma_select]['titulos']['filtros_produtos'],
                    size = vg.size_letra_titulos, color = c.texto_principal,
                    font_family = 'inter'
                )
            ]
        )
        self.space_tags.controls.clear()
        self.space_tags.controls.extend(self.lista_tags)
        self.lista_scroll_tag = ft.Column(
            spacing = 16,
            expand = True,
            scroll = ft.ScrollMode.AUTO,
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.START,
            controls = [
                self.titulo_tags,
                self.space_tags,
            ]
        )
        self.lista_controls_tag = ft.Column(
            expand = True,
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                self.lista_scroll_tag,
                
                ft.Container(
                    height = vg.size_botoes,
                    border_radius = vg.raio_borda,
                    alignment = ft.Alignment.CENTER,
                    gradient = c.gradiente_top_bottom(colors = c.gradiente_botoes),

                    content = ft.Text(
                        value = dic.palavras[dic.idioma_select]['atendimento']['salvar'],
                        size = vg.size_letra_destaque, color = c.fundo_neutralo if c.tema == 'claro' else c.fundo,
                        font_family = 'inter'
                    ),

                    ink = True,
                    on_click = self.recarregar_produtos,

                    margin = ft.Margin(
                        top = vg.margin_top,
                        left = vg.margin_left,
                        right = vg.margin_right,
                        bottom = 24
                    )
                )
            ]
        )

        self.titulo_tikets = ft.Row(
            height = 54,
            alignment = ft.MainAxisAlignment.CENTER,
            vertical_alignment = ft.CrossAxisAlignment.END,
            controls = [
                ft.Text(
                    value = dic.palavras[dic.idioma_select]['titulos']['tikets'],
                    size = vg.size_letra_titulos, color = c.texto_principal,
                    font_family = 'inter'
                )
            ]
        )
        self.column_cupom = ft.Column(
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.START,
        )
        self.campo_desconto = ft.TextField(
            expand = True,
            border_radius = vg.raio_borda,
            border_color = c.texto_suave,
            focused_border_color = c.cor_principal,
            border = ft.Border.all(width = 0.8, color = c.texto_suave),
            text_style = ft.TextStyle(size = vg.size_letra_normal, color = c.texto_principal, font_family = 'inter'),
            label_style = ft.TextStyle(
                size = vg.size_letra_destaque, color = c.texto_suave,
                font_family = 'inter',
            ),

            margin = ft.Margin(left = vg.margin_left, right = vg.margin_right),

            label = dic.palavras[dic.idioma_select]['atendimento']['desconto'],

            on_focus = self.campo_on,
            on_blur = self.campo_off,
            keyboard_type = ft.KeyboardType.DATETIME,

            key = ft.ScrollKey(f'Key_{dic.palavras[dic.idioma_select]['atendimento']['desconto']}'),
            prefix_style = ft.TextStyle(size = vg.size_letra_normal, color = c.texto_principal, font_family = 'inter'),
            suffix_style = ft.TextStyle(size = vg.size_letra_normal, color = c.texto_principal, font_family = 'inter'),
            prefix = vg.moedas_format[dic.idioma_select][5] if vg.moedas_format[dic.idioma_select][5] != ' €' else None,
            suffix = vg.moedas_format[dic.idioma_select][5] if vg.moedas_format[dic.idioma_select][5] == ' €' else None,
        )
        self.campo_cupom = ft.TextField(
            expand = True,
            border_radius = 28,
            border_color = c.texto_suave,
            focused_border_color = c.cor_principal,
            border = ft.Border.all(width = 0.8, color = c.texto_suave),
            text_style = ft.TextStyle(size = vg.size_letra_normal, color = c.texto_principal, font_family = 'inter'),
            label_style = ft.TextStyle(
                size = vg.size_letra_destaque, color = c.texto_suave,
                font_family = 'inter',
            ),

            margin = ft.Margin(left = vg.margin_left, right = vg.margin_right),

            label = dic.palavras[dic.idioma_select]['atendimento']['cupom'],

            data = {'coluna': self.column_cupom,},

            on_focus = self.campo_on,
            on_blur = self.campo_loading,
            on_change = self.text_maiusculo,

            key = ft.ScrollKey(f'Key_{dic.palavras[dic.idioma_select]['atendimento']['adicional']}'),
            prefix_style = ft.TextStyle(size = vg.size_letra_normal, color = c.texto_principal, font_family = 'inter'),
            prefix = 'N° '
        )
        self.column_cupom.controls.append(self.campo_cupom)
        self.lista_scroll_tikets = ft.Column(
            spacing = 20,
            scroll = ft.ScrollMode.AUTO,
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                self.titulo_tikets,
                self.campo_desconto,
                self.column_cupom,
            ]
        )
        self.lista_controls_tikets = ft.Column(
            expand = True,
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                self.lista_scroll_tikets,

                ft.Container(
                    height = vg.size_botoes,
                    border_radius = vg.raio_borda,
                    alignment = ft.Alignment.CENTER,
                    gradient = c.gradiente_top_bottom(colors = c.gradiente_botoes),

                    content = ft.Text(
                        value = dic.palavras[dic.idioma_select]['atendimento']['salvar'],
                        size = vg.size_letra_destaque, color = c.fundo_neutralo if c.tema == 'claro' else c.fundo,
                        font_family = 'inter'
                    ),

                    ink = True,
                    on_click = True,

                    margin = ft.Margin(
                        top = vg.margin_top,
                        left = vg.margin_left,
                        right = vg.margin_right,
                        bottom = 24
                    )
                )
            ]
        )

    def text_maiusculo(self, e):
        e.control.value = str(e.control.value).upper()
        e.control.update()

    async def campo_loading(self, e):
        verifid_completo = ft.Row(
            alignment = ft.MainAxisAlignment.START,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                ft.ProgressRing(width = 18, height = 18, color = c.cor_principal, stroke_width = 2),
                ft.Text(
                    value = 'Verificando código...',
                    size = vg.size_letra_destaque, color = c.cor_principal, font_family = 'inter'
                )
            ],

            margin = ft.Margin(left = vg.margin_left, right = vg.margin_right)
        )

        if verifid_completo not in e.control.data['coluna'].controls:
            e.control.data['coluna'].controls.append(verifid_completo)

        self.campo_off(e)

        self.page.update()

    async def campo_on(self, e):
        e.control.label_style = ft.TextStyle(
            size = vg.size_letra_destaque, color = c.cor_principal,
            font_family = 'inter',
        )

        await vg.scrollagem_key(column_row = self.lista_controls_tikets, key = e.control.key)

    def campo_off(self, e):
        if e.control.value == '':
            e.control.label_style = ft.TextStyle(
                size = vg.size_letra_normal, color = c.texto_suave,
                font_family = 'inter',
            )

        else:
            e.control.label_style = ft.TextStyle(
                size = vg.size_letra_destaque, color = c.texto_suave,
                font_family = 'inter',
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

    def recarregar_produtos(self, e):
        self.lista_scroll.controls.clear()

        if len(self.lista_tags_ativas) >= 1:
            for tag in self.lista_tags_ativas:
                if tag.data['tag'] in vg.servicos_carregados:
                    for x in vg.servicos_carregados[tag.data['tag']]:
                        control_box = vg.servicos_carregados[tag.data['tag']][x]['control']

                        item_filtrado = control_box
                        self.lista_scroll.controls.append(item_filtrado)

        elif len(self.lista_tags_ativas) == 0:
            for x in vg.servicos_carregados[vg.todos_txt]:
                control_box = vg.servicos_carregados[vg.todos_txt][x]['control']
                
                self.lista_scroll.controls.append(control_box)

        self.fechar_PopUp(e)
        self.page.update()

    def box_ativo(self, ativar = None, box = None, update = True):
        if box != None:
            if ativar == True:
                box.data['ativo'] = False

            elif ativar == False:
                box.data['ativo'] = True

            if box.data['tag'] != vg.todos_txt:
                box.bgcolor = c.fundo_neutralo

                if box.data['ativo'] == False:
                    if box not in self.lista_tags_ativas:
                        self.lista_tags_ativas.append(box)

                    box.data['ativo'] = True
                    box.opacity = 1.0
                    box.content.controls[0].color = c.cor_principal
                    box.border = ft.Border.all(width = 1.6, color = c.cor_principal)

                else:
                    if box in self.lista_tags_ativas:
                        self.lista_tags_ativas.remove(box)

                    box.opacity = 0.6
                    box.data['ativo'] = False
                    box.content.controls[0].color = c.texto_suave
                    box.border = ft.Border.all(width = 0.8, color = c.texto_suave)

            else:
                if box.data['ativo'] == False:
                    if box not in self.lista_tags_ativas:
                        self.lista_tags_ativas.append(box)

                    box.opacity = 1.0
                    box.data['ativo'] = True
                    box.bgcolor = c.cor_principal
                    box.content.controls[0].color = c.fundo_neutralo if c.tema == 'claro' else c.fundo
                    box.border = ft.Border.all(width = 0.8, color = ft.Colors.TRANSPARENT)

                else:
                    if box in self.lista_tags_ativas:
                        self.lista_tags_ativas.remove(box)

                    box.opacity = 0.6
                    box.data['ativo'] = False
                    box.bgcolor = c.fundo_neutralo
                    box.content.controls[0].color = c.texto_suave
                    box.border = ft.Border.all(width = 0.8, color = c.texto_suave)

        if update:
            box.update()

    def selecao_tags(self, e):
        box_e = e.control

        if box_e.data['tag'] != vg.todos_txt:
            self.box_ativo(box = box_e)

            for x in self.lista_tags_ativas:
                if x.data['tag'] == vg.todos_txt:
                    self.box_ativo(ativar = False, box = x)
                    x.update()

        if box_e.data['tag'] == vg.todos_txt or (len(self.lista_tags) - 1) == len(self.lista_tags_ativas):
            if box_e.data['tag'] == vg.todos_txt and box_e.data['ativo'] == True:
                self.box_ativo(box = box_e)
                box_e.update()
                return
            
            for x in self.lista_tags:
                self.box_ativo(ativar = False, box = x)

                if x.data['tag'] == vg.todos_txt:
                    self.box_ativo(box = x)

        self.page.update()

    def width_tag(self, texto = 'None', size = 16, fator = 0.62):
        return int(len(texto) * size * fator) + 40
    
    def abrir_PopUp(self, e):
        self.space_tags.width = self.page.width - (2 * vg.margin_left)

        vg.box_PopUp.controls[1].content = None
        vg.conteudo_box_PopUp(self.page, conteudo = self.lista_controls_tag)
        vg.box_PopUp.controls[1].shadow = c.shadow_leve()
        vg.box_PopUp.controls[1].bgcolor = c.fundo_neutralo
        vg.box_PopUp.visible = True
        self.page.update()

    def fechar_PopUp(self, e):
        vg.box_PopUp.visible = False
        vg.box_PopUp.controls[1].content = None
        self.page.update()

    def abrir_aba_tikets(self, e):
        vg.box_PopUp.controls[1].content = None
        vg.box_PopUp.controls[1].shadow = c.shadow_leve()
        vg.box_PopUp.controls[1].bgcolor = c.fundo_neutralo
        vg.conteudo_box_PopUp(page = self.page, conteudo = self.lista_controls_tikets)
        vg.box_PopUp.visible = True
        self.page.update()

    def decimal(self, valor = None, text_yn = False):
        return conv.Moedas().decimal_n(valor = valor, p_texto = text_yn)

    def conversor(self, valor = None, decimal = None, text_yn = False, cifrao = False):
        if valor is not None:
            valor = str(valor)
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
                        btn_click.bgcolor = c.cor_principal
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
            size = vg.size_letra_destaque, color = c.texto_principal, text_align = ft.TextAlign.CENTER,
            font_family = 'inter', margin = ft.Margin(left = 8, right = 8)
        )

        botao_menos = ft.Container(
            data = {},
            width = vg.size_botoes * 6 / 7,
            height = vg.size_botoes * 6 / 7,
            opacity = 0.2,
            border_radius = vg.raio_borda,
            shadow = c.shadow_leve(opc = 0.56),
            bgcolor = c.fundo_neutralo,
            alignment = ft.Alignment.CENTER,

            content = ft.Icon(
                icon = ft.CupertinoIcons.MINUS,
                size = vg.size_icons, color = c.texto_principal,
            ),

            ink = False,
            on_click = acao_botoes_quantidae
        )

        botao_mais = ft.Container(
            data = {},
            width = vg.size_botoes * 6 / 7,
            height = vg.size_botoes * 6 / 7,
            border_radius = vg.raio_borda,
            bgcolor = c.fundo_alternativo,
            alignment = ft.Alignment.CENTER,
            margin = ft.Margin(right = vg.margin_right),

            content = ft.Icon(
                icon = ft.CupertinoIcons.PLUS,
                size = vg.size_icons, color = c.texto_principal,
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
                        margin = ft.Margin(left = vg.margin_left),
                        alignment = ft.MainAxisAlignment.CENTER,
                        horizontal_alignment = ft.CrossAxisAlignment.START,

                        controls = [
                            ft.Text(
                                value = servico,
                                size = vg.size_letra_destaque, color = c.texto_principal,
                                font_family = 'inter'
                            ),

                            ft.Row(
                                spacing = 0,
                                alignment = ft.MainAxisAlignment.START,
                                vertical_alignment = ft.CrossAxisAlignment.CENTER,
                                controls = [
                                    ft.Text(
                                        value = self.conversor(valor = valor, text_yn = True),
                                        size = vg.size_letra_normal, color = c.texto_secundario,
                                        font_family = 'inter'
                                    )
                                ]
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

        if dic.idioma_select in ['FR', 'ES']:
            box.content.controls[0].controls[1].controls.append(
                ft.Text(
                    value = vg.moedas_format[dic.idioma_select][5],
                    size = vg.size_letra_normal, color = c.texto_secundario,
                    font_family = 'inter'
                )
            )

        else:
            box.content.controls[0].controls[1].controls.insert(
                0,
                ft.Text(
                    value = vg.moedas_format[dic.idioma_select][5],
                    size = vg.size_letra_normal, color = c.texto_secundario,
                    font_family = 'inter'
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
            width = vg.size_botoes,
            height = vg.size_botoes,
            border_radius = vg.raio_borda,
            shadow = c.shadow_leve(),
            bgcolor = c.cor_principal,
            alignment = ft.Alignment.CENTER,
            margin = ft.Margin(right = vg.margin_right),

            content = ic.svg_icon(
                'filtro',
                size = vg.size_icons, color = c.fundo_neutralo
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
            border_radius = vg.raio_borda,
            margin = ft.Margin(left = vg.margin_left, right = vg.margin_right),
            shadow = c.shadow_leve(),
            bgcolor = c.fundo_neutralo,
            alignment = ft.Alignment.CENTER,
            content = self.lista_scroll,
            height = self.page.height * 0.44,
        )

        titulo_subtotal = ft.Text(
            value = dic.palavras[dic.idioma_select]['atendimento']['subtotal'],
            size = vg.size_letra_normal, color = c.texto_secundario, font_family = 'inter'
        )

        texto_subtotal = ft.Text(
            value = vg.moedas_format[vg.moeda_ativa][0],
            size = vg.size_letras_valores_destaque, color = c.texto_principal, font_family = 'inter'
        )

        cifrao = ft.Text(
            value = vg.moedas_format[vg.moeda_ativa][5],
            size = vg.size_letras_valores_destaque, color = c.texto_principal, font_family = 'inter'
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

        btn_tiket = ft.Container(
            width = vg.size_botoes,
            height = vg.size_botoes,
            border_radius = vg.raio_borda,
            shadow = c.shadow_leve(),
            bgcolor = c.cor_principal,
            content = ic.svg_icon(
                icon = 'tiket',
                size = vg.size_icons, color = c.fundo_neutralo if c.tema == 'claro' else c.fundo
            ),
            alignment = ft.Alignment.CENTER,
            margin = ft.Margin(right = vg.margin_right),

            ink = True,
            on_click = self.abrir_aba_tikets
        )

        row_subtotal_tikets = ft.Row(
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                subtotal_completo,
                btn_tiket
            ]
        )

        btn_prosseguir = ft.Container(
            height = vg.size_botoes,
            expand = True,
            bgcolor = c.fundo,
            border_radius = vg.raio_borda,
            shadow = c.shadow_leve(),
            alignment = ft.Alignment.CENTER,
            border = ft.Border.all(width = 0.6, color = c.texto_suave),
            margin = ft.Margin(left = vg.margin_left, right = vg.margin_right),
            
            content = ft.Text(
                value = dic.palavras[dic.idioma_select]['atendimento']['prosseguir'],
                size = vg.size_letra_destaque, color = c.texto_suave, font_family = 'inter',
                weight = ft.FontWeight.NORMAL
            ),

            ink = True,
            on_click = None,
        )

        for x in vg.servicos_carregados[vg.todos_txt]:
            setor = vg.servicos_carregados[vg.todos_txt][x]['setor']
            valor = vg.servicos_carregados[vg.todos_txt][x]['valor']
            produto = vg.servicos_carregados[vg.todos_txt][x]['produto']

            control_box = self.box_servicos(
                setor = setor,
                valor = valor,
                servico = produto,
                lista = self.lista_scroll,
                text_subtotal = texto_subtotal,
                botao_presseguir = btn_prosseguir
            )

            self.lista_scroll.controls.append(control_box)
            vg.servicos_carregados[vg.todos_txt][x]['control'] = control_box
            vg.servicos_carregados[setor][x]['control'] = control_box

        lista.controls[0].controls.extend([
            vg.barra_pesquisa(
                text_interno = dic.palavras[dic.idioma_select]['atendimento']['busca_rapida'],
                on_change = lambda e: vg.sistema_de_busca(
                    e,
                    self.page,
                    self.lista_scroll,
                    vg.servicos_carregados[vg.todos_txt],
                    busca_servico = True, lista_tags = self.lista_tags,
                    funcao_tag = self.box_ativo
                )
            ),

            btn_filtro
        ])

        lista.controls.append(box_lista)
        lista.controls.append(row_subtotal_tikets)
        lista.controls.append(btn_prosseguir)
        lista.controls.append(ft.Column(height = 360))

        return lista