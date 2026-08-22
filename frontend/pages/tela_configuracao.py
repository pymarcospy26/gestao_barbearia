import flet as ft
import icons as ic
import colors as c
import banco as bd
import play_audio as play
import variaveis_globais as vg
import dicionario_idioma as dic

class Configuracao:
    def __init__(
        self,
        page: ft.Page,
        fx_tela_idioma,
    ):
        self.page = page
        self.tema_da_page = bd.status_tema_page(option = 0)

        self.fx_Tela_Idioma = fx_tela_idioma

    def tela_config(self):
        return self.estrutua_setings()

    async def alternar_tema(self, e):
        if e.control.value == True:
            bd.status_tema_page(tema = 'escuro', option = 1)
            
        else:
            bd.status_tema_page(tema = 'claro', option = 1)

        await c.carregar_tema()
        await vg.pagina_main()
        vg.cor_btns_navegation_bar(None, 'tema/escuro/claro')
        await vg.pagina_configuracao_main(None)

    def buttons_config(
        self,
        sub_text_config = 'This is config One',
        text_config = 'Config one',
        icon_config = 'coffe',
        switch_change = None,
        color_action = None,
        switch_value = True,
        icon_action = None,
        switch = False,
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
                            ic.svg_icon(
                                icon_config,
                                size = 30, color = c.texto_secundario,
                            ),

                            ft.Column(
                                spacing = 0,
                                margin = ft.Margin(left = 8),
                                alignment = ft.MainAxisAlignment.CENTER,
                                horizontal_alignment = ft.CrossAxisAlignment.START,

                                controls = [
                                    ft.Text(
                                        expand = True,
                                        value = text_config,
                                        size = vg.size_letra_destaque, color = c.texto_principal,
                                        font_family = 'inter',
                                        max_lines = 1, overflow = ft.TextOverflow.ELLIPSIS
                                    ),

                                    ft.Text(
                                        expand = True,
                                        value = sub_text_config,
                                        size = vg.size_letra_normal, color = c.texto_secundario,
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

        if switch == True:
            switch_control = ft.CupertinoSwitch(
                value = switch_value,
                active_track_color = c.cor_principal,
                data = {'control': 'switch'},
                on_change = switch_change
            )

            button.content.controls.insert(1, switch_control)

        else:
            if icon_action == None:
                button.content.controls.insert(
                    1,
                    ic.svg_icon(
                        'seta_right',
                        size = 30, color = c.texto_suave
                    )
                )
            else:
                button.content.controls.insert(
                    1,
                    ic.svg_icon(
                        icon_action,
                        size = 30, color = color_action if color_action != None else c.cor_amarelo
                    )
                )
        return button

    def boxs_config(self, controls = []):
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

    def estrutua_setings(self):
        coluna = ft.Column(
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,

            controls = [
                self.boxs_config(
                    controls = [
                        self.buttons_config(
                            text_config = dic.palavras[dic.idioma_select]['configuracao']['empresa'],
                            sub_text_config = dic.palavras[dic.idioma_select]['configuracao']['info_empresa'],
                            icon_config = 'empresa', click = True,
                        ),

                        self.buttons_config(
                            text_config = dic.palavras[dic.idioma_select]['configuracao']['administracao'],
                            sub_text_config = dic.palavras[dic.idioma_select]['configuracao']['controle_acessos'],
                            icon_config = 'adm', click = True, 
                        ),

                    ]
                ),
                
                self.boxs_config(
                    controls = [
                        self.buttons_config(
                            text_config = dic.palavras[dic.idioma_select]['configuracao']['tema_escuro'],
                            sub_text_config = dic.palavras[dic.idioma_select]['configuracao']['alternar_tema'],
                            icon_config = 'lua', switch = True, switch_change = self.alternar_tema, switch_value = True if self.tema_da_page == 'escuro' else False
                        ),

                        self.buttons_config(
                            text_config = dic.palavras[dic.idioma_select]['configuracao']['idioma'],
                            sub_text_config = dic.palavras[dic.idioma_select]['configuracao']['alterar_idioma'],
                            icon_config = 'idioma', click = self.fx_Tela_Idioma, 
                        ),

                    ]
                ),

                ft.Column(
                    height = 360
                )
            ]
        )

        return coluna