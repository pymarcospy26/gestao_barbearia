import flet as ft
import banco as bd
import colors as c
import imagens as img
import variaveis_globais as vg
import dicionario_idioma as dic

class Tela_Idioma:
    def __init__(self, page: ft.Page):
        self.page = page

    def tela_idioma(self):
        pass

    def box_idiomas(self, controls = []):
        box = ft.Container(
            border_radius = 34,
            bgcolor = c.fundo_neutralo,
            shadow = c.shadow_leve(),
            content = ft.Column(
                spacing = 0,
                alignment = ft.MainAxisAlignment.START,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            ),
            margin = ft.Margin(
                top = vg.margin_top,
                left = vg.margin_left,
                right = vg.margin_right
            )
        )

        box.content.controls.extend(controls)

        controles_inseridos = len(box.content.controls)
        if controles_inseridos == 1:
            box.border_radius = 28

        if controles_inseridos > 1:
            for i, x in enumerate(box.content.controls, 1):
                if i == 1:
                    x.height = 94
                    x.padding = ft.Padding(top = 24, left = 24, right = 24, bottom = 12)
                elif i == controles_inseridos:
                    x.height = 94
                    x.padding = ft.Padding(top = 12, left = 24, right = 24, bottom = 24)
                else:
                    x.height = 82
                    x.padding = ft.Padding(top = 12, left = 24, right = 24, bottom = 12)

        return box

    async def br_idioma(self, e):
        await self.idiomas('BR')

    async def eua_idiomas(self, e):
        await self.idiomas('EUA')

    async def es_idiomas(self, e):
        await self.idiomas('ES')

    async def fr_idiomas(self, e):
        await self.idiomas('FR')

    async def idiomas(self, idioma = 'BR'):
        bd.status_idioma_page(idioma = idioma, option = 1)
        dic.idioma_select = idioma
        vg.moeda_ativa = idioma
        await vg.pagina_main()
        vg.cor_btns_navegation_bar(None, 'idiomas')
        await vg.pagina_idioma(None)

    def buttons_idioma(
        self,
        text_idioma = 'Português BR',
        img_idioma = 'Brasil',
        click = None,
    ):

        button = ft.Container(
            height = 94,
            padding = 26,
            bgcolor = c.fundo_neutralo,
            content = ft.Row(
                spacing = 0,
                alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment = ft.CrossAxisAlignment.CENTER,

                controls = [
                    ft.Row(
                        expand = True,
                        alignment = ft.MainAxisAlignment.START,
                        vertical_alignment = ft.CrossAxisAlignment.CENTER,

                        controls = [
                            img.image_idioma(
                                img_idioma,
                            ),

                            ft.Column(
                                spacing = 0,
                                margin = ft.Margin(left = 8),
                                alignment = ft.MainAxisAlignment.CENTER,
                                horizontal_alignment = ft.CrossAxisAlignment.START,

                                controls = [
                                    ft.Text(
                                        value = text_idioma,
                                        size = 16, color = c.texto_principal,
                                        font_family = 'inter',
                                        max_lines = 1, overflow = ft.TextOverflow.ELLIPSIS
                                    ),
                                ]
                            )
                        ]
                    )
                ]
            ),

            ink = True,
            on_click = click
        )

        return button

    def tela(self):
        return self.estrutura()

    def estrutura(self):
        coluna = ft.Column(
            spacing = 0,
            expand = True,
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,

            controls = [
                self.box_idiomas(
                    controls = [
                        self.buttons_idioma(
                            text_idioma = dic.palavras[dic.idioma_select]['idioma']['nome_idioma']['portugues'],
                            img_idioma = 'Brasil', click = self.br_idioma
                        ),

                        self.buttons_idioma(
                            text_idioma = dic.palavras[dic.idioma_select]['idioma']['nome_idioma']['ingles'],
                            img_idioma = 'EUA', click = self.eua_idiomas
                        ),

                        self.buttons_idioma(
                            text_idioma = dic.palavras[dic.idioma_select]['idioma']['nome_idioma']['espanhol'],
                            img_idioma = 'Espanha', click = self.es_idiomas
                        ),

                        self.buttons_idioma(
                            text_idioma = dic.palavras[dic.idioma_select]['idioma']['nome_idioma']['frances'],
                            img_idioma = 'França', click = self.fr_idiomas
                        ),
                    ]
                ),

                self.box_idiomas(
                    controls = [
                        ft.Row(
                            expand = True,
                            alignment = ft.MainAxisAlignment.START,
                            vertical_alignment = ft.CrossAxisAlignment.CENTER,
                            margin = 25,
                            controls = [
                                ft.Text(
                                    expand = True,
                                    value = dic.palavras[dic.idioma_select]['idioma']['exemplo'],
                                    size = 16, color = c.texto_secundario,
                                    font_family = 'inter', overflow = ft.TextOverflow.CLIP
                                )
                            ]
                        )
                    ]
                )
            ]
        )

        return coluna