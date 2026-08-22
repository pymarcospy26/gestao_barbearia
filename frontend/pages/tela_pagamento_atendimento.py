import flet as ft
import colors as c
import icons as ic
import conversores as conv
import variaveis_globais as vg
import dicionario_idioma as dic

class Pagamento:
    def __init__(self, page: ft.Page):
        self.page = page

    def espaco_x_field(self):
        return ft.Container(height = 0, visible = False)

    def box_pagamentos(
        self,
        taxas = 0,
        tipo_pagamento = None,
        icon_pagamento = None,
        left = 0, right = 0,
        posicao = None,
        btn_salvar = None,
        row_pag = None,
        coluna_controls = None
    ):
        
        def click_pagamentos(e):
            box = e.control
            if box.data['btn_ativo'] == False:
                box.bgcolor = None
                box.gradient = c.gradiente_top_bottom(colors = c.gradiente_botoes)
                box.border = ft.Border.all(width = 0, color = ft.Colors.TRANSPARENT)
                box.content.controls[0].color = c.fundo if c.tema == 'escuro' else c.fundo_neutralo
                box.content.controls[1].color = c.fundo if c.tema == 'escuro' else c.fundo_neutralo
                box.content.controls[1].weight = ft.FontWeight.W_600

                coluna_controls.controls[posicao] = box.data['campo_inserir_valor']

            else:
                box.bgcolor = c.fundo
                box.gradient = None
                box.border = ft.Border.all(width = 0.8, color = c.texto_suave)
                box.content.controls[0].color = c.texto_suave
                box.content.controls[1].color = c.texto_suave
                box.content.controls[1].weight = ft.FontWeight.NORMAL

                coluna_controls.controls[posicao] = self.espaco_x_field()

            box.data['btn_ativo'] = not box.data['btn_ativo']

            btn_ativos_w = []
            for x in row_pag.controls:
                btn_ativos_w.append(str(x.data['btn_ativo']))

            if 'True' in btn_ativos_w:
                btn_salvar.bgcolor = None
                btn_salvar.gradient = c.gradiente_top_bottom(colors = c.gradiente_botoes)
                btn_salvar.border = ft.Border.all(width = 0, color = ft.Colors.TRANSPARENT)
                btn_salvar.content.weight = ft.FontWeight.W_600
                btn_salvar.content.color = c.fundo_neutralo if c.tema == 'claro' else c.fundo
                btn_salvar.on_click = True

            else:
                btn_salvar.bgcolor = c.fundo
                btn_salvar.gradient = None
                btn_salvar.border = ft.Border.all(width = 0.6, color = c.texto_suave)
                btn_salvar.content.weight = ft.FontWeight.NORMAL
                btn_salvar.content.color = c.texto_suave
                btn_salvar.on_click = None
            
            self.page.update()

        box = ft.Container(
            border = ft.Border.all(width = 0.8, color = c.texto_suave),
            alignment = ft.Alignment.CENTER,
            height = self.page.height * 0.1264,
            shadow = c.shadow_leve(),
            border_radius = 28,
            bgcolor = c.fundo,
            col = 1,

            content = ft.Column(
                spacing = 0,
                alignment = ft.MainAxisAlignment.CENTER,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                controls = [
                    ic.svg_icon(
                        icon = icon_pagamento,
                        size = 28, color = c.texto_suave
                    ),
                    ft.Text(
                        value = tipo_pagamento, weight = ft.FontWeight.NORMAL,
                        size = vg.size_letra_destaque, color = c.texto_suave, font_family = 'inter'
                    ),
                ]
            ),

            ink = True,
            on_click = click_pagamentos,

            data = {},

            margin = ft.Margin(left = left, right = right)
        )

        box.data['box'] = box
        box.data['taxa'] = taxas
        box.data['btn_ativo'] = False
        box.data['pagamento'] = tipo_pagamento

        async def campo_on(e):
            e.control.label_style = ft.TextStyle(
                size = 20, color = c.cor_principal,
                font_family = 'inter',
            )

            await vg.scrollagem_key(column_row = vg.page_croll_main, key = e.control.key)

        def campo_off(e):
            if e.control.value == '':
                e.control.label_style = ft.TextStyle(
                    size = 16, color = c.texto_suave,
                    font_family = 'inter',
                )

            else:
                e.control.label_style = ft.TextStyle(
                    size = 20, color = c.texto_suave,
                    font_family = 'inter',
                )

        campo_box = ft.TextField(
            expand = True,
            border_radius = 28,
            border_color = c.texto_suave,
            focused_border_color = c.cor_principal,
            value = vg.moedas_format[dic.idioma_select][0],
            border = ft.Border.all(width = 0.8, color = c.texto_suave),
            text_style = ft.TextStyle(size = 18, color = c.texto_principal, font_family = 'inter'),
            label_style = ft.TextStyle(
                size = 20, color = c.texto_suave,
                font_family = 'inter',
            ),

            margin = ft.Margin(left = vg.margin_left, right = vg.margin_right),

            label = f'{dic.palavras[dic.idioma_select]['atendimento']['recebido']} {tipo_pagamento}',

            content_padding = ft.Padding(
                top = 24.5,
                left = 24.5,
                right = 24.5,
                bottom = 24.5,
            ),

            on_focus = campo_on,
            on_blur = campo_off,

            key = ft.ScrollKey(f'Key_{tipo_pagamento}'),
            prefix_style = ft.TextStyle(size = 20, color = c.texto_principal, font_family = 'inter'),
            suffix_style = ft.TextStyle(size = 20, color = c.texto_principal, font_family = 'inter'),
            prefix = vg.moedas_format[dic.idioma_select][5] if vg.moedas_format[dic.idioma_select][5] != ' €' else None,
            suffix = vg.moedas_format[dic.idioma_select][5] if vg.moedas_format[dic.idioma_select][5] == ' €' else None,
        )

        box.data['campo_inserir_valor'] = campo_box

        return box

    def tela(self):
        return self.lista()

    def lista(self):
        coluna_controles = ft.Column(
            spacing = 16,
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.START,
        )

        row_pagamentos = ft.ResponsiveRow(
            columns = 2,
            spacing = 16,
            run_spacing = 16,
            margin = ft.Margin(top = vg.margin_top, bottom = vg.margin_top),
            alignment = ft.MainAxisAlignment.START,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,
        )

        btn_salvar = ft.Container(
            height = 74,
            bgcolor = c.fundo,
            border_radius = 28,
            alignment = ft.Alignment.CENTER,
            border = ft.Border.all(width = 0.6, color = c.texto_suave),
            content = ft.Text(
                value = dic.palavras[dic.idioma_select]['atendimento']['salvar'],
                size = vg.size_letra_destaque, color = c.texto_suave, weight = ft.FontWeight.NORMAL
            ),
            margin = ft.Margin(top = vg.margin_top, left = vg.margin_left, right = vg.margin_right)
        )

        row_pagamentos.controls.extend([
            self.box_pagamentos(
                tipo_pagamento = dic.palavras[dic.idioma_select]['atendimento']['dinheiro'],
                icon_pagamento = 'dinheiro', left = vg.margin_left, posicao = 1,
                btn_salvar = btn_salvar, row_pag = row_pagamentos, coluna_controls = coluna_controles
            ),

            self.box_pagamentos(
                tipo_pagamento = dic.palavras[dic.idioma_select]['atendimento']['cartao'],
                icon_pagamento = 'cartao', right = vg.margin_right, posicao = 2,
                btn_salvar = btn_salvar, row_pag = row_pagamentos, coluna_controls = coluna_controles
            ),

            self.box_pagamentos(
                tipo_pagamento = dic.palavras[dic.idioma_select]['atendimento']['digital'],
                icon_pagamento = 'pagamento_digital', left = vg.margin_left, posicao = 3,
                btn_salvar = btn_salvar, row_pag = row_pagamentos, coluna_controls = coluna_controles
            ),

            self.box_pagamentos(
                tipo_pagamento = dic.palavras[dic.idioma_select]['atendimento']['outros'],
                icon_pagamento = 'tres_pontos', right = vg.margin_right, posicao = 4,
                btn_salvar = btn_salvar, row_pag = row_pagamentos, coluna_controls = coluna_controles
            )
        ])

        coluna_controles.controls.extend([
            row_pagamentos,
            self.espaco_x_field(),
            self.espaco_x_field(),
            self.espaco_x_field(),
            self.espaco_x_field(),
            btn_salvar,
            ft.Column(height = 560)
        ])

        self.page.update()

        return coluna_controles