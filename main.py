import flet as ft
import icons as ic
import colors as c

import play_audio as play
import variaveis_globais as vg
import dicionario_idioma as dic

from backend import fluxo_telas as fx

from frontend.pages import tela_home as thm
from frontend.pages import tela_configuracao as tcg
from frontend.pages import tela_mudar_idioma as tid
from frontend.pages import tela_atendimento_dialog as diag
from frontend.pages import tela_atendimento_normal as norm
from frontend.pages import tela_registros_atendimentos as tra

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.data = {}
        self.page.padding = 0

        self.page.bgcolor = c.fundo
        self.quantidade_home = 0
        self.quantidade_agenda = 0
        self.quantidade_historico = 0
        self.quantidade_configuracao = 0
        self.lista_btns_control_bar = []

        self.page.fonts = {
            'inter': 'fonts/Inter-VariableFont_opsz,wght.ttf'
        }

        if c.tema == 'claro':
            self.page.theme = ft.Theme(
                system_overlay_style = ft.SystemOverlayStyle(
                    status_bar_color = ft.Colors.TRANSPARENT,
                    status_bar_icon_brightness = ft.Brightness.DARK,

                    system_navigation_bar_color = ft.Colors.TRANSPARENT,
                    system_navigation_bar_icon_brightness = ft.Brightness.DARK
                )
            )

            print('tema claro')

        elif c.tema == 'escuro':
            self.page.theme = ft.Theme(
                system_overlay_style = ft.SystemOverlayStyle(
                    status_bar_color = ft.Colors.TRANSPARENT,
                    status_bar_icon_brightness = ft.Brightness.LIGHT,

                    system_navigation_bar_color = ft.Colors.TRANSPARENT,
                    system_navigation_bar_icon_brightness = ft.Brightness.LIGHT
                )
            )

            print('tema escuro')

        self.tela_home = thm.Tela_Home(page)

        self.titulo_control = ft.Text(
            value = 'HELLO WORD',
            size = 26, color = c.texto_principal,
            font_family = 'inter', weight = ft.FontWeight.W_400
        )
        self.box_titulo = ft.Container(
            height = 74,
            bgcolor = ft.Colors.TRANSPARENT,
            alignment = ft.Alignment.CENTER,
            content = self.titulo_control,
            margin = ft.Margin(top = vg.margin_top)
        )

        self.button_bar_center = ft.Column(
            col = 3,
            spacing = 0,
            alignment = ft.MainAxisAlignment.CENTER,
            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                ft.Container(
                    width = 92,
                    height = 92,
                    border_radius = 92 / 2,
                    margin = ft.Margin(top = 26, bottom = 32),

                    gradient = c.gradiente_top_bottom(c.gradiente_banner),

                    shadow = ft.BoxShadow(
                        blur_radius = 10,
                        offset = ft.Offset(0, 4),
                        color = ft.Colors.with_opacity(color = c.cor_principal_escura, opacity = 0.4)
                    ),

                    alignment = ft.Alignment.CENTER,

                    content = ft.Icon(
                        icon = ft.CupertinoIcons.SCISSORS_ALT,
                        size = 35, color = c.fundo_neutralo
                    ),

                    ink = True,
                    on_click = self.tela_atendimento_GO
                )
            ]
        )

        self.control_bar = ft.Container(
            left = 0,
            right = 0,
            bottom = 0,
            expand = True,
            bgcolor = c.fundo_neutralo,
            alignment = ft.Alignment.CENTER,
            shadow = c.shadow_leve(0, -4, opc = 0.36),

            content = ft.ResponsiveRow(
                columns = 11,
                spacing = 0,
                expand = True,
                alignment = ft.MainAxisAlignment.CENTER,
                vertical_alignment = ft.CrossAxisAlignment.CENTER,

                controls = [
                    ft.Container(
                        col = 2,
                        height = 92,
                        expand = True,
                        border_radius = 92 / 2,
                        bgcolor = ft.Colors.TRANSPARENT,
                        alignment = ft.Alignment.CENTER,
                        content = ft.Column(
                            spacing = 0,
                            data = {'controle': dic.palavras[dic.idioma_select]['titulos']['inicio']},
                            alignment = ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                            
                            controls = [
                                ft.Container(width = 10, height = 10, border_radius = 5, bgcolor = ft.Colors.TRANSPARENT),
                                ic.svg_icon('home', size = 30, color = c.cor_principal),
                                ft.Text(value = dic.palavras[dic.idioma_select]['titulos']['inicio'], size = 14, color = c.cor_principal, font_family = 'inter', weight = ft.FontWeight.W_500, margin = ft.Margin(top = 2)),
                                ft.Container(width = 10, height = 10, border_radius = 5, bgcolor = c.cor_principal, margin = ft.Margin(top = 6)),
                            ]
                        ),
                        ink = True,
                        on_click = self.tela_home_GO
                    ),

                    ft.Container(
                        col = 2,
                        height = 92,
                        expand = True,
                        border_radius = 92 / 2,
                        bgcolor = ft.Colors.TRANSPARENT,
                        alignment = ft.Alignment.CENTER,
                        content = ft.Column(
                            spacing = 0,
                            data = {'controle': dic.palavras[dic.idioma_select]['titulos']['agenda']},
                            alignment = ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                            
                            controls = [
                                ft.Container(width = 10, height = 10, border_radius = 5, bgcolor = ft.Colors.TRANSPARENT),
                                ic.svg_icon('calendar', size = 30, color = c.texto_suave),
                                ft.Text(value = dic.palavras[dic.idioma_select]['titulos']['agenda'], size = 14, color = c.texto_suave, weight = ft.FontWeight.W_500, font_family = 'inter', margin = ft.Margin(top = 2)),
                                ft.Container(width = 10, height = 10, border_radius = 5, bgcolor = c.texto_suave, margin = ft.Margin(top = 6)),
                            ]
                        ),
                        ink = True,
                        on_click = self.tela_agenda_GO
                    ),

                    self.button_bar_center,

                    ft.Container(
                        col = 2,
                        height = 92,
                        expand = True,
                        border_radius = 92 / 2,
                        bgcolor = ft.Colors.TRANSPARENT,
                        alignment = ft.Alignment.CENTER,
                        content = ft.Column(
                            spacing = 0,
                            data = {'controle': dic.palavras[dic.idioma_select]['titulos']['historico']},
                            alignment = ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                            
                            controls = [
                                ft.Container(width = 10, height = 10, border_radius = 5, bgcolor = ft.Colors.TRANSPARENT),
                                ic.svg_icon('historico', size = 30, color = c.texto_suave),
                                ft.Text(value = dic.palavras[dic.idioma_select]['titulos']['historico'], size = 14, color = c.texto_suave, weight = ft.FontWeight.W_500, font_family = 'inter', margin = ft.Margin(top = 2)),
                                ft.Container(width = 10, height = 10, border_radius = 5, bgcolor = c.texto_suave, margin = ft.Margin(top = 6)),
                            ]
                        ),
                        ink = True,
                        on_click = self.tela_historico_GO
                    ),

                    ft.Container(
                        col = 2,
                        height = 92,
                        expand = True,
                        border_radius = 92 / 2,
                        bgcolor = ft.Colors.TRANSPARENT,
                        alignment = ft.Alignment.CENTER,
                        content = ft.Column(
                            spacing = 0,
                            data = {'controle': dic.palavras[dic.idioma_select]['titulos']['outros']},
                            alignment = ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                            
                            controls = [
                                ft.Container(width = 10, height = 10, border_radius = 5, bgcolor = ft.Colors.TRANSPARENT),
                                ic.svg_icon('tres_pontos', size = 30, color = c.texto_suave),
                                ft.Text(value = dic.palavras[dic.idioma_select]['titulos']['outros'], size = 14, color = c.texto_suave, weight = ft.FontWeight.W_500, font_family = 'inter', margin = ft.Margin(top = 2)),
                                ft.Container(width = 10, height = 10, border_radius = 5, bgcolor = ft.Colors.TRANSPARENT, margin = ft.Margin(top = 6)),
                            ]
                        ),
                        ink = True
                    ),
                ]
            )
        )

        self.lista_btns_control_bar.extend([
            self.control_bar.content.controls[0].content,
            self.control_bar.content.controls[1].content,
            self.control_bar.content.controls[3].content,
            self.control_bar.content.controls[4].content,
        ])

        self.tela_scrol = ft.Column(
            top = 0,
            left = 0,
            right = 0,
            bottom = 0,
            
            expand = True,
            scroll = ft.ScrollMode.AUTO,
            alignment = ft.MainAxisAlignment.START,

            controls = [
                ft.Row( 
                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment = ft.CrossAxisAlignment.CENTER,
                    controls = [
                        self.botoes_top('menu', margin_top = vg.margin_top, margin_left = vg.margin_left, on_click = self.tela_configuracao_GO, data = 'Configuracao'),
                        self.box_titulo,
                        self.stack_notificcao('sino', None, margin_top = vg.margin_top, margin_right = vg.margin_right, data = 'Notificação')
                    ]
                ),

                ft.Column(height = 200) #espaco pra empurrar os componentes a baixo da bar
            ]
        )

        self.area_page = ft.Column(
            spacing = 0,
            expand = True,
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.START,
            controls = []
        )

        vg.page_croll_main = self.tela_scrol
        vg.area_page_main = self.area_page
        
        self.tela_scrol.controls.insert(1, self.area_page)

        self.estrutura = ft.Stack(
            expand = True,
            controls = [
                self.tela_scrol,
                self.control_bar,
            ]
        )

        self.page.data['area_build'] = self.area_page

    def click_cor_control_bar(self, e, controle = None):
        for x in self.lista_btns_control_bar:
            if x.data['controle'] == controle:
                x.controls[1].color = c.cor_principal_escura
                x.controls[2].color = c.cor_principal_escura
                x.controls[3].bgcolor = c.cor_principal_escura

            else:
                x.controls[1].color = c.texto_suave
                x.controls[2].color = c.texto_suave
                x.controls[3].bgcolor = ft.Colors.TRANSPARENT

    async def troca_de_pagina(self, e, pagina = None, titulo = None, icon_config = 'menu', preservar_anterior = False, clear = True):
        if clear:
            for x in self.tela_scrol.controls[1:]:
                self.tela_scrol.controls.remove(x)
            self.tela_scrol.controls.append(self.area_page)

        self.mudar_button_config_EXIT_MENU(icon = icon_config)
        self.click_cor_control_bar(e, controle = titulo)
        tela_go = pagina
        if preservar_anterior == False: vg.tela_anterior = tela_go
        self.titulo_control.value = dic.palavras[dic.idioma_select]['titulos'][titulo]
        self.area_page.controls.clear()
        self.area_page.controls.append(tela_go)
        self.click_cor_control_bar(e, controle = dic.palavras[dic.idioma_select]['titulos'][titulo])
        self.page.update()

    def botoes_top(
        self,
        icon = 'menu', on_click = None, data = 'config',
        top = None, left = None, right = None, bottom = None,
        margin_top = 0, margin_left = 0, margin_right = 0, margin_bottom = 0
    ):
        return ft.Container(
            top = top,
            left = left,
            right = right,
            bottom = bottom,
            data = {'controle': data},
            width = 74,
            height = 74,
            bgcolor = c.fundo_neutralo,
            border_radius = 28,
            shadow = c.shadow_leve(),
            alignment = ft.Alignment.CENTER,
            margin = ft.Margin(
                top = margin_top,
                left = margin_left,
                right = margin_right,
                bottom = margin_bottom
            ),
            content = ic.svg_icon(icon, size = 30, color = c.texto_secundario),
            on_click = on_click, ink = True
        )
    def stack_notificcao(
        self,
        icon = 'sino', on_click = None, data = 'notificacao',
        margin_top = 0, margin_left = 0, margin_right = 0, margin_bottom = 0
    ):
        btn = self.botoes_top(
            icon = icon,
            on_click = on_click,
            right = 0, bottom = 0,
            data = data
        )
        stack = ft.Stack(
            data = {},
            width = 74,
            height = 74,
            controls = [
                btn,
                ft.Container(
                    top = 0,
                    left = 0,
                    width = 18,
                    height = 18,
                    border_radius = 9,
                    bgcolor = c.cor_principal_escura,
                )
            ],
            margin = ft.Margin(
                top = margin_top,
                left = margin_left,
                right = margin_right,
                bottom = margin_bottom
            )
        )
        btn.data['stack'] = stack
        stack.data['btn'] = btn
        return stack
    def mudar_button_config_EXIT_MENU(self, icon = 'menu'):
        self.tela_scrol.controls[0] = ft.Row(
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment = ft.CrossAxisAlignment.START,
            controls = [
                self.botoes_top(icon, margin_top = vg.margin_top, margin_left = vg.margin_left, on_click = self.tela_configuracao_GO, data = 'Configuracao'),
                self.box_titulo,
                self.stack_notificcao('sino', None, margin_top = vg.margin_top, margin_right = vg.margin_right, data = 'Notificação')
            ]
        )
    async def recriar_main(self, page_go = None):
        self.page.controls.clear()
        async def page_page(page: ft.Page):
            novo_app = App(page)
            await novo_app.abrir_home()

        await page_page(self.page)

        if page_go != None:
            pass

    async def devolver_atendimento(self, e):
        async def voltar_atendimento(e):
            if vg.pagina_ativa_go == vg.pagina_atendimento_go:
                vg.btn_centro.on_click = vg.nova_tela_atendimento
                vg.btn_centro.content = ic.svg_icon(
                    icon = 'vassoura', size = 34, color = c.fundo_neutralo
                )

            else:
                async def voltar_atendimento_salvo(e):
                    await self.troca_de_pagina(
                        e, pagina = vg.pagina_atendimento_go,
                        titulo = 'atendimento', icon_config = 'menu',
                        clear = False if vg.pagina_ativa_go == vg.pagina_pagamento_go else True
                    )

                    vg.go_pagamento_aprovd = False
                    vg.pagina_ativa_go = vg.pagina_atendimento_go

                    vg.btn_centro.on_click = vg.nova_tela_atendimento
                    vg.btn_centro.content = ic.svg_icon(
                        icon = 'vassoura', size = 34, color = c.fundo_neutralo
                    )

                    self.page.update()

                vg.btn_centro.on_click = voltar_atendimento_salvo
                vg.btn_centro.content = ic.svg_icon(
                    icon = 'seta_exit', size = 34, color = c.fundo_neutralo
                )
            
            await self.troca_de_pagina(
                e, pagina = vg.pagina_ativa_go,
                titulo = 'atendimento', icon_config = 'menu',
                clear = False if vg.pagina_ativa_go == vg.pagina_pagamento_go else True
            )

        if vg.btn_centro != None and vg.pagina_atendimento_go != None:
            vg.btn_centro.on_click = voltar_atendimento
            vg.btn_centro.content = ft.Icon(
                icon = ft.CupertinoIcons.SCISSORS_ALT,
                size = 35, color = c.fundo_neutralo
            )

        self.page.update()

    async def tela_home_GO(self, e):
        await self.troca_de_pagina(
            e, pagina = await thm.Tela_Home(self.page).tela(),
            titulo = 'inicio'
        )

        await self.devolver_atendimento(e)
    async def tela_atendimento_GO(self, e):
        vg.btn_centro = self.button_bar_center.controls[0]
        vg.btn_centro.on_click = vg.nova_tela_atendimento
        vg.btn_centro.content = ic.svg_icon(
            icon = 'vassoura', size = 34, color = c.fundo_neutralo
        )

        await vg.carregar_dados()
        vg.pagina_atendimento_go = norm.Tela_Atendimento(self.page).tela()
        vg.pagina_ativa_go = vg.pagina_atendimento_go

        await self.troca_de_pagina(
            e, pagina = vg.pagina_atendimento_go,
            titulo = 'atendimento'
        )
    async def tela_agenda_GO(self, e):
        await self.troca_de_pagina(
            e, pagina = ft.Container(),
            titulo = 'agenda'
        )

        await self.devolver_atendimento(e)
    async def tela_historico_GO(self, e):
        await self.troca_de_pagina(
            e, pagina = tra.Registro_Atendimentos(self.page).tela(),
            titulo = 'historico'
        )
        
        await self.devolver_atendimento(e)
    async def tela_configuracao_GO(self, e):
        await self.troca_de_pagina(
            e, pagina = tcg.Configuracao(self.page, self.tela_idioma_GO).tela_config(),
            titulo = 'configuracao'
        )
        
        await self.devolver_atendimento(e)
    async def tela_idioma_GO(self, e):
        await self.troca_de_pagina(
            e, pagina = tid.Tela_Idioma(self.page).tela(),
            titulo = 'idioma',
            preservar_anterior = True, icon_config = 'seta_exit'
        )
        
        await self.devolver_atendimento(e)

    async def abrir_home(self):
        async def nova_tela_atendimento(e):
            vg.go_pagamento_aprovd = False
            vg.pagina_ativa_go = None
            vg.pagina_pagamento_go = None
            vg.pagina_atendimento_go = None
            await self.tela_atendimento_GO(e)
        vg.nova_tela_atendimento = nova_tela_atendimento
        vg.troca_de_pagina = self.troca_de_pagina
        vg.pagina_main = self.recriar_main
        vg.pagina_agenda = self.tela_agenda_GO
        vg.pagina_idioma = self.tela_idioma_GO
        vg.pagina_configuracao_main = self.tela_configuracao_GO
        vg.cor_btns_navegation_bar = self.click_cor_control_bar

        await self.tela_home_GO(None)
        await play.system_sons(self.page)
        self.page.add(
            ft.SafeArea(
                height = self.page.height,
                content = ft.Column(
                    height = self.page.height,
                    alignment = ft.MainAxisAlignment.START,
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                    controls = [self.estrutura]
                )
            )
        )

async def execute( page: ft.Page):
    i = App(page)  
    await i.abrir_home()

ft.run(execute, assets_dir = 'assets')
# ft.run(execute, view = ft.AppView.WEB_BROWSER, host = '0.0.0.0', assets_dir = 'assets')