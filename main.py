import flet as ft
import icons as ic
import colors as c
import play_audio as play
import variaveis_globais as vg
from backend import fluxo_telas as fx
from frontend.pages import tela_home as thm
from frontend.pages import tela_atendimento_dialog as diag
from frontend.pages import tela_registros_atendimentos as tra

class App:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.data = {}
        self.page.padding = 0

        self.titulos_page = 'HELLO WORD'
        self.page.bgcolor = c.background
        self.quantidade_home = 0
        self.quantidade_agenda = 0
        self.quantidade_historico = 0
        self.lista_btns_control_bar = []

        self.page.fonts = {
            'inter': 'fonts/Inter-VariableFont_opsz,wght.ttf'
        }
        self.page.theme = ft.Theme(
            system_overlay_style = ft.SystemOverlayStyle(
                status_bar_color = ft.Colors.TRANSPARENT,
                status_bar_icon_brightness = ft.Brightness.DARK,

                system_navigation_bar_color = c.branco,
                system_navigation_bar_icon_brightness = ft.Brightness.DARK
            )
        )
        self.tela_home = thm.Tela_Home(page)

        def botoes_top(
            icon = 'menu', on_click = None,
            top = None, left = None, right = None, bottom = None,
            margin_top = 0, margin_left = 0, margin_right = 0, margin_bottom = 0
        ):
            return ft.Container(
                top = top,
                left = left,
                right = right,
                bottom = bottom,

                data = {},
                width = 74,
                height = 74,
                bgcolor = c.branco,
                border_radius = 28,
                shadow = c.shadow_leve(),
                alignment = ft.Alignment.CENTER,
                margin = ft.Margin(
                    top = margin_top,
                    left = margin_left,
                    right = margin_right,
                    bottom = margin_bottom
                ),
                content = ic.svg_icon(icon, size = 30, color = c.sub_textos),

                on_click = on_click
            )
        def stack_notificcao(
            icon = 'sino', on_click = None,
            margin_top = 0, margin_left = 0, margin_right = 0, margin_bottom = 0
        ):
            btn = botoes_top(
                icon = icon,
                on_click = on_click,
                right = 0, bottom = 0,
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
                        bgcolor = c.azul_violeta,
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

        self.titulo_control = ft.Text(
            value = self.titulos_page,
            size = 26, color = c.preto_icons,
            font_family = 'inter', weight = ft.FontWeight.W_400
        )
        self.box_titulo = ft.Container(
            height = 74,
            bgcolor = ft.Colors.TRANSPARENT,
            alignment = ft.Alignment.CENTER,
            content = self.titulo_control,
            margin = ft.Margin(top = vg.margin_top)
        )

        self.button_bar_center = ft.Container(
            col = 1,
            width = 100,
            height = 100,
            border_radius = 50,
            margin = ft.Margin(top = 22, bottom = 24),

            gradient = c.gradiente_top_bottom(c.gradiente_banner),

            shadow = ft.BoxShadow(
                blur_radius = 10,
                offset = ft.Offset(0, 4),
                color = ft.Colors.with_opacity(color = c.azul_violeta, opacity = 0.4)
            ),

            alignment = ft.Alignment.CENTER,

            content = ft.Icon(
                icon = ft.CupertinoIcons.SCISSORS_ALT,
                size = 35, color = c.branco
            ),

            ink = True,
            on_click = self.abrir_atendimento
        )

        self.control_bar = ft.Container(
            left = 0,
            right = 0,
            bottom = 0,
            expand = True,
            bgcolor = c.branco,
            alignment = ft.Alignment.CENTER,
            shadow = c.shadow_leve(0, -4, opc = 0.36),

            content = ft.ResponsiveRow(
                columns = 5,
                spacing = 0,
                expand = True,
                alignment = ft.MainAxisAlignment.CENTER,
                vertical_alignment = ft.CrossAxisAlignment.CENTER,

                controls = [
                    ft.Container(
                        col = 1,
                        height = 100,
                        expand = True,
                        border_radius = 50,
                        bgcolor = ft.Colors.TRANSPARENT,
                        alignment = ft.Alignment.CENTER,
                        content = ft.Column(
                            spacing = 0,
                            data = {'controle': 'Início'},
                            alignment = ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                            
                            controls = [
                                ft.Container(width = 10, height = 10, border_radius = 5, bgcolor = ft.Colors.TRANSPARENT),
                                ic.svg_icon('home', size = 32, color = c.roxo),
                                ft.Text(value = 'Início', size = 14, color = c.roxo, font_family = 'inter', weight = ft.FontWeight.W_600, margin = ft.Margin(top = 2)),
                                ft.Container(width = 10, height = 10, border_radius = 5, bgcolor = c.roxo, margin = ft.Margin(top = 6)),
                            ]
                        ),
                        ink = True,
                        on_click = self.tela_home_GO
                    ),

                    ft.Container(
                        col = 1,
                        height = 100,
                        expand = True,
                        border_radius = 50,
                        bgcolor = ft.Colors.TRANSPARENT,
                        alignment = ft.Alignment.CENTER,
                        content = ft.Column(
                            spacing = 0,
                            data = {'controle': 'Agenda'},
                            alignment = ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                            
                            controls = [
                                ft.Container(width = 10, height = 10, border_radius = 5, bgcolor = ft.Colors.TRANSPARENT),
                                ic.svg_icon('calendar', size = 32, color = c.txt_fra),
                                ft.Text(value = 'Agenda', size = 14, color = c.txt_fra, font_family = 'inter', margin = ft.Margin(top = 2)),
                                ft.Container(width = 10, height = 10, border_radius = 5, bgcolor = c.txt_fra, margin = ft.Margin(top = 6)),
                            ]
                        ),
                        ink = True,
                        on_click = self.tela_agenda_GO
                    ),

                    self.button_bar_center,

                    ft.Container(
                        col = 1,
                        height = 100,
                        expand = True,
                        border_radius = 50,
                        bgcolor = ft.Colors.TRANSPARENT,
                        alignment = ft.Alignment.CENTER,
                        content = ft.Column(
                            spacing = 0,
                            data = {'controle': 'Histórico'},
                            alignment = ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                            
                            controls = [
                                ft.Container(width = 10, height = 10, border_radius = 5, bgcolor = ft.Colors.TRANSPARENT),
                                ic.svg_icon('historico', size = 32, color = c.txt_fra),
                                ft.Text(value = 'Histórico', size = 14, color = c.txt_fra, font_family = 'inter', margin = ft.Margin(top = 2)),
                                ft.Container(width = 10, height = 10, border_radius = 5, bgcolor = c.txt_fra, margin = ft.Margin(top = 6)),
                            ]
                        ),
                        ink = True,
                        on_click = self.tela_historico_GO
                    ),

                    ft.Container(
                        col = 1,
                        height = 100,
                        expand = True,
                        border_radius = 50,
                        bgcolor = ft.Colors.TRANSPARENT,
                        alignment = ft.Alignment.CENTER,
                        content = ft.Column(
                            spacing = 0,
                            data = {'controle': 'Mais'},
                            alignment = ft.MainAxisAlignment.CENTER,
                            horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                            
                            controls = [
                                ft.Container(width = 10, height = 10, border_radius = 5, bgcolor = ft.Colors.TRANSPARENT),
                                ic.svg_icon('tres_pontos', size = 32, color = c.txt_fra),
                                ft.Text(value = 'Outros', size = 14, color = c.txt_fra, font_family = 'inter', margin = ft.Margin(top = 2)),
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

            controls = [
                ft.Row(
                    expand = True,
                    alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                    vertical_alignment = ft.CrossAxisAlignment.CENTER,
                    controls = [
                        botoes_top('menu', None, margin_top = vg.margin_top, margin_left = vg.margin_left),
                        self.box_titulo,
                        stack_notificcao('sino', None, margin_top = vg.margin_top, margin_right = vg.margin_right)
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
                x.controls[1].color = c.roxo_esc
                x.controls[2].color = c.roxo_esc
                x.controls[3].bgcolor = c.roxo_esc

            else:
                x.controls[1].color = c.txt_fra
                x.controls[2].color = c.txt_fra
                x.controls[3].bgcolor = ft.Colors.TRANSPARENT
                
    async def abrir_atendimento(self, e):
        alert_dialog = diag.AlertDialog_atendimento(self.page)
        await alert_dialog.inicializar()
        alert_dialog.abrir(e)

    async def tela_home_GO(self, e):
        self.click_cor_control_bar(e, controle = 'Início')
        tela_home_go = await self.tela_home.tela()
        fx.tela_anterior = tela_home_go
        self.quantidade_home += 1
        self.titulo_control.value = await self.tela_home.titulo() + str(self.quantidade_home)
        self.area_page.controls.clear()
        self.area_page.controls.append(tela_home_go)
        # await fx.mudar_page(
        #     page = self.page,
        #     atual = tela_inicio,         USAR ESSE MODELO PARA NAVEGAÇÃO INTERNA
        #     anterior = tela_inicio,
        #     nova = tela_nova
        # )(e)
        self.page.update()
    async def tela_agenda_GO(self, e):
        self.click_cor_control_bar(e, controle = 'Agenda')
        tela_agenda_go = ft.Container(expand = True, bgcolor = c.verde)
        fx.tela_anterior = tela_agenda_go
        self.quantidade_agenda += 1
        self.titulo_control.value = 'Agenda' + str(self.quantidade_agenda)
        self.area_page.controls.clear()
        self.area_page.controls.append(tela_agenda_go)
        self.page.update()
    async def tela_historico_GO(self, e):
        self.click_cor_control_bar(e, controle = 'Histórico')
        tela_historico_go = tra.Registro_Atendimentos(self.page).tela()
        fx.tela_anterior = tela_historico_go
        self.quantidade_historico += 1
        self.titulo_control.value = 'Histórico' + str(self.quantidade_historico)
        self.area_page.controls.clear()
        self.area_page.controls.append(tela_historico_go)
        self.page.update()
    async def abrir_home(self):
        await self.tela_home_GO(None)
        await play.system_sons(self.page)
        self.page.add(
            ft.SafeArea(
                expand = True,
                content = self.estrutura
            )
        )
  
async def execute( page: ft.Page):
    i = App(page)  
    await i.abrir_home()

# ft.run(execute, assets_dir = 'assets')
ft.run(execute, view = ft.AppView.WEB_BROWSER, host = '0.0.0.0', assets_dir = 'assets')