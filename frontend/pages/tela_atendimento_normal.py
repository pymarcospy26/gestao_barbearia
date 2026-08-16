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

        self.barra_pesquisa_servicos = self.barra_pesquisa_fx(on_blur = self.fechar_teclado, on_focus = self.abrir_teclado)

    async def abrir_teclado(self, e):
        await vg.ativar_teclado_virtual(e, self.barra_pesquisa_servicos.controls[0].content)

    async def fechar_teclado(self, e):
        await vg.desativar_teclado_virtual(e)
        
    # def pesquisa_servicos(self, e):
    #     digitado = e.control.value
    #     # self.alertdialog_global.data['lista_atendimento'].controls.clear() - ÁREA DE LISTA

    #     controles = []

    #     def normalizar_letras(texto):
    #         texto = unicodedata.normalize('NFD', texto)
    #         texto = ''.join(
    #             letra
    #             for letra in texto
    #             if unicodedata.category(letra) != 'Mn'
    #         )

    #         return texto.lower()

    #     palavras_busca = normalizar_letras(digitado).split()

    #     for servico in self.armazenamento_controles:
    #         texto_servico = normalizar_letras(servico)

    #         if all(palavra in texto_servico for palavra in palavras_busca):
    #             self.alertdialog_global.data['lista_atendimento'].alignment = ft.MainAxisAlignment.START
    #             controles.append(self.armazenamento_controles[servico])

    #     if len(controles) == 0:
    #         not_found = ft.Column(
    #             alignment = ft.MainAxisAlignment.CENTER,
    #             horizontal_alignment = ft.CrossAxisAlignment.CENTER,
    #             controls = [
    #                 ic.svg_icon(
    #                     'not_found_busca',
    #                     size = 50, color = c.texto_principal
    #                 ),

    #                 ft.Text(
    #                     value = dic.palavras[dic.idioma_select]['atendimento']['sem_resultados'],
    #                     size = 16, color = c.texto_principal,
    #                     font_family = 'inter', text_align = ft.TextAlign.CENTER
    #                 ),
    #             ]
    #         )

    #         self.alertdialog_global.data['lista_atendimento'].alignment = ft.MainAxisAlignment.CENTER
    #         self.alertdialog_global.data['lista_atendimento'].controls.append(not_found)

    #         return
        
    #     self.alertdialog_global.data['lista_atendimento'].controls.extend(controles)

    def barra_pesquisa_fx(
        self,
        text_interno = dic.palavras[dic.idioma_select]['atendimento']['busca_rapida'],

        on_blur:ft.Event = None,
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
                    bgcolor = c.fundo_neutralo,
                    border_radius = 24,
                    shadow = c.shadow_leve(),
                    
                    margin = ft.Margin(
                        left = vg.margin_left, right = vg.margin_right
                    ),

                    content = ft.TextField(
                        expand = True,
                        border_radius = 24,
                        content_padding = ft.Padding(top = 21, bottom = 21),

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

                        keyboard_type = ft.KeyboardType.NONE
                    )
                ),
                
                ic.svg_icon(
                    path = 'lupa',
                    size = 30, color = c.texto_suave,
                    left = 38
                )
            ]
        )

    def box_servicos(
        self,
        setor = 'setor not found',
        servico = 'servico not found',
        valor = 'valor not found'
    ):

        campo = ft.Text(
            value = 0,
            size = 16, color = c.texto_principal,
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

            ink = True,
        )

        botao_mais = ft.Container(
            data = {},
            width = 56,
            height = 56,
            opacity = 0.2,
            border_radius = 24,
            shadow = c.shadow_leve(),
            bgcolor = c.fundo_neutralo,
            alignment = ft.Alignment.CENTER,
            margin = ft.Margin(right = 26),

            content = ft.Icon(
                icon = ft.CupertinoIcons.PLUS,
                size = 24, color = c.texto_principal,
            ),

            ink = True,
        )

        control_quantidade = ft.Row(
            data = {},
            spacing = 0,
            alignment = ft.MainAxisAlignment.CENTER,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,

            controls = [
                botao_menos,
                campo,
                botao_mais,
            ]
        )

        botao_mais.data = {
            'campo': campo,
            'botao_mais': botao_mais,
            'botao_menos': botao_menos,
            'control_quantidade': control_quantidade,
        }
        
        botao_menos.data = {
            'campo': campo,
            'botao_mais': botao_mais,
            'botao_menos': botao_menos,
            'control_quantidade': control_quantidade,
        }
        
        control_quantidade.data = {
            'campo': campo,
            'botao_mais': botao_mais,
            'botao_menos': botao_menos,
            'control_quantidade': control_quantidade,
        }
     
        box = ft.Container(
            height = 86,
            expand = True,
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

        return box

    def tela(self):
        return self.lista()

    def lista(self):
        lista = ft.Column(
            spacing = 16,
            expand = True,
            margin = ft.Margin(top = vg.margin_top),
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,

            controls = [
                self.barra_pesquisa_servicos
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
            margin = vg.margin_top,
            shadow = c.shadow_leve(),
            bgcolor = c.fundo_neutralo,
            alignment = ft.Alignment.CENTER,
            content = lista_scroll
        )

        for x in self.servicos_carregados['todos']:
            control_box = self.box_servicos(
                setor = self.servicos_carregados['todos'][x]['setor'],
                valor = self.servicos_carregados['todos'][x]['valor'],
                servico = self.servicos_carregados['todos'][x]['produto']
            )

            lista_scroll.controls.append(control_box)
            self.controls_servicos_carregados.append(control_box)

        lista.controls.append(box_lista)

        return lista
















