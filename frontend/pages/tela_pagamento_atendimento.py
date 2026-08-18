import flet as ft
import colors as c
import icons as ic
import conversores as conv
import variaveis_globais as vg
import dicionario_idioma as dic

class Pagamento:
    def __init__(self, page: ft.Page):
        self.page = page

    def box_pagamentos(
            self,
            taxas = 0,
            tipo_pagamento = None,
            icon_pagamento = None,
            multiplas_formas = None,
            left = 0, right = 0,
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

            else:
                box.bgcolor = c.fundo
                box.gradient = None
                box.border = ft.Border.all(width = 0.8, color = c.texto_suave)
                box.content.controls[0].color = c.texto_suave
                box.content.controls[1].color = c.texto_suave
                box.content.controls[1].weight = ft.FontWeight.NORMAL

            box.data['btn_ativo'] = not box.data['btn_ativo']
            self.page.update()

        box = ft.Container(
            border = ft.Border.all(width = 0.8, color = c.texto_suave),
            alignment = ft.Alignment.CENTER,
            height = self.page.height * 0.14,
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
                        size = 16, color = c.texto_suave, font_family = 'inter'
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

        return box

    def tela(self):
        return self.lista()

    def lista(self):
        lista_controls = ft.Column(
            spacing = 0,
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.START,
            controls = [
                self.box_pagamentos(
                    tipo_pagamento = dic.palavras[dic.idioma_select]['dialog_atendimento']['dinheiro'],
                    icon_pagamento = 'dinheiro', left = vg.margin_left
                ),

                self.box_pagamentos(
                    tipo_pagamento = dic.palavras[dic.idioma_select]['dialog_atendimento']['cartao'],
                    icon_pagamento = 'cartao', right = vg.margin_right
                ),

                self.box_pagamentos(
                    tipo_pagamento = dic.palavras[dic.idioma_select]['dialog_atendimento']['digital'],
                    icon_pagamento = 'pagamento_digital', left = vg.margin_left
                ),

                self.box_pagamentos(
                    tipo_pagamento = dic.palavras[dic.idioma_select]['dialog_atendimento']['outros'],
                    icon_pagamento = 'tres_pontos', right = vg.margin_right
                ),
            ]
        )

        return lista_controls











