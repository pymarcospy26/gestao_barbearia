import flet as ft
import icons as ic
import banco as bd
import colors as c
import unicodedata
import variaveis_globais as vg
import dicionario_idioma as dic

class Tela_Atendimento:
    def __init__(self, page: ft.Page):
        self.page = page

        self.servicos_carregados = vg.servicos_carregados
        self.controls_servicos_carregados = []

    def barra_pesquisa_fx(
        self,
        text_interno = dic.palavras[dic.idioma_select]['atendimento']['busca_rapida'],

        on_blur:ft.Event = None,
        on_focus: ft.Event = None,
        on_change: ft.Event = None,
    ):
        return ft.Stack(
            height = 78,
            expand = True,
            alignment = ft.Alignment.TOP_CENTER,

            controls = [
                ft.Container(
                    left = 0,
                    right = 0,
                    expand = True,
                    bgcolor = c.fundo_neutralo,
                    border_radius = 28,
                    shadow = c.shadow_leve(),
                    
                    margin = ft.Margin(
                        left = vg.margin_left
                    ),

                    content = ft.TextField(
                        expand = True,
                        border_radius = 28,
                        content_padding = ft.Padding(top = 24.5, bottom = 24.5),

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

                        text_align = ft.TextAlign.CENTER,

                        on_blur = on_blur,
                        on_focus = on_focus,
                        on_change = on_change,
                    )
                ),
                
                ic.svg_icon(
                    path = 'lupa',
                    size = 30, color = c.texto_suave,
                    left = 38, top = 0, bottom = 4
                )
            ]
        )

    def box_servicos(
        self,
        setor = 'setor not found',
        servico = 'servico not found',
        valor = 'valor not found',
        lista: ft.Control = None,
    ):
        
        async def acao_botoes_quantidae(e):
            btn_click = e.control
            campo_text = btn_click.data['campo']
            btn_mais = btn_click.data['botao_mais']
            btn_menos = btn_click.data['botao_menos']

            subiu_yn = btn_click.data['subiu']
            box_clik = btn_click.data['box']
            key_box = btn_click.data['key']
            lista = btn_click.data['lista']

            if btn_click.data['x'] == 'menos':
                if int(campo_text.value) >= 1:
                    campo_text.value = int(campo_text.value) - 1

                    if int(campo_text.value) == 0:
                        btn_mais.shadow = None
                        btn_mais.bgcolor = c.fundo_alternativo
                        btn_mais.content.color = c.texto_principal

                        btn_click.opacity = 0.2
                        btn_click.ink = False 

            if btn_click.data['x'] == 'mais':
                campo_text.value = int(campo_text.value) + 1

                if int(campo_text.value) >= 1:
                    btn_click.bgcolor = c.cor_principal_escura
                    btn_click.shadow = c.shadow_leve()
                    btn_click.content.color = c.fundo_neutralo

                    btn_menos.opacity = 1
                    btn_menos.ink = True

                    if subiu_yn == False:
                        lista.controls.remove(box_clik)
                        lista.controls.insert(0, box_clik)

                        await vg.scrollagem(
                            offset = 0,
                            column_row = lista,
                            time = 350
                        )

                        btn_click.data['subiu'] = True

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
            shadow = c.shadow_leve(),
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
            on_click = True,
        )

        lista = ft.Column(
            spacing = 16,
            expand = True,
            margin = ft.Margin(top = vg.margin_top),
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,

            controls = [
                ft.Row(
                    spacing = 16,
                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment = ft.CrossAxisAlignment.START,
                    controls = [
                        self.barra_pesquisa_fx(
                            text_interno = dic.palavras[dic.idioma_select]['atendimento']['busca_rapida']
                        ),
                        btn_filtro
                    ]
                )
            ]
        )

        lista_scroll = ft.Column(
            spacing = 0,
            expand = True,
            scroll = ft.ScrollMode.AUTO,
            alignment = ft.MainAxisAlignment.START,
            margin = ft.Margin(top = 8, bottom = 8),
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
        )

        box_lista = ft.Container(
            expand = True,
            border_radius = 28,
            margin = ft.Margin(left = vg.margin_left, right = vg.margin_right),
            shadow = c.shadow_leve(),
            bgcolor = c.fundo_neutralo,
            alignment = ft.Alignment.CENTER,
            content = lista_scroll
        )

        for x in self.servicos_carregados['todos']:
            control_box = self.box_servicos(
                setor = self.servicos_carregados['todos'][x]['setor'],
                valor = self.servicos_carregados['todos'][x]['valor'],
                servico = self.servicos_carregados['todos'][x]['produto'],
                lista = lista_scroll
            )

            lista_scroll.controls.append(control_box)
            self.controls_servicos_carregados.append(control_box)

        lista.controls.append(box_lista)

        return lista
















