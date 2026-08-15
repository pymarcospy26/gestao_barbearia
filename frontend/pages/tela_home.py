import flet as ft
import colors as c
import icons as ic
import variaveis_globais as vg
import dicionario_idioma as dic

class Tela_Home:
    def __init__(self, page: ft.Page):
        self.page = page
        self.agendamentos = {
            'João Guilherme': {
                'hora': '10:40',
                'setor': 'Estética',
                'servico': 'Design de Sobrancelha',
                'cor_urgencia': c.cor_vermelho
            },

            'Maria Eduarda': {
                'hora': '13:20',
                'setor': 'Barbearia',
                'servico': 'Hidratação Capilar',
                'cor_urgencia': c.cor_laranja
            },

            'Ana Carolina': {
                'hora': '16:15',
                'setor': 'Estética',
                'servico': 'Drenagem Linfática',
                'cor_urgencia': c.cor_principal_clara
            }
        }
        self.titulo_pages = 'Home'
        self.acesso_rapido = [dic.palavras[dic.idioma_select]['home']['retirada'], dic.palavras[dic.idioma_select]['home']['fiados'], dic.palavras[dic.idioma_select]['home']['agendar']]

    async def titulo(self):
        return self.titulo_pages
    
    async def tela(self):
        self.banner = ft.Container(
            height = 360,
            expand = True,
            border_radius = 34,
            bgcolor = c.fundo_neutralo,
            shadow = c.shadow_leve(),
            margin = ft.Margin(left = vg.margin_left, top = vg.margin_top, right = vg.margin_right),
            # gradient = c.gradiente_top_bottom(c.gradiente_banner),
        )
        self.ferramentas = ft.ResponsiveRow(
            spacing = 0,
            columns = 3,
            expand = True,
            run_spacing = 0,
            
            alignment = ft.MainAxisAlignment.START,
            vertical_alignment = ft.CrossAxisAlignment.START,

            controls = []
        )

        def btns_ferramentas(titulo, icon, r = 0, l = 0, t = 0, b = 0, col = 1):
            self.ferramentas.controls.append(
                ft.Container(
                    col = col,
                    height = 140,
                    bgcolor = c.fundo_neutralo,
                    border_radius = 34,
                    margin = ft.Margin(left = l, right = r, top = t, bottom = b),

                    shadow = c.shadow_leve(),

                    alignment = ft.Alignment.CENTER,
                    
                    content = ft.Column(
                        alignment = ft.MainAxisAlignment.CENTER,
                        horizontal_alignment = ft.CrossAxisAlignment.CENTER,

                        controls = [
                            ic.svg_icon(
                                icon,
                                size = 30,
                                color = c.texto_secundario
                            ),
                            
                            ft.Text(
                                value = titulo,
                                size = 16, color = c.texto_secundario, weight = ft.FontWeight.W_400,
                                font_family = 'inter', text_align = ft.TextAlign.CENTER
                            )
                        ]
                    ),

                    on_click = True,
                    ink = True
                )
            )
        btns_ferramentas(self.acesso_rapido[0], 'retirada_caixa', l = vg.margin_left, r = vg.margin_right / 2, t = vg.margin_top + 10, col = 1)
        btns_ferramentas(self.acesso_rapido[1], 'fiados', l = vg.margin_left / 2, r = vg.margin_right / 2, t = vg.margin_top + 10, col = 1)
        btns_ferramentas(self.acesso_rapido[2], 'calendar_add', l = vg.margin_left / 2, r = vg.margin_right, t = vg.margin_top + 10, col = 1)

        self.agendados_prox = ft.Column(
            spacing = 0,

            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.START,

            controls = [
                ft.Text(
                    value = dic.palavras[dic.idioma_select]['home']['clientes_agendados'],
                    size = 20, color = c.texto_secundario,
                    font_family = 'inter', margin = ft.Margin(
                        left = vg.margin_left, top = vg.margin_top, bottom = vg.margin_top
                    )
                ),

                ft.ResponsiveRow(
                    columns = 2,
                    spacing = 0,
                    run_spacing = 16,

                    alignment = ft.MainAxisAlignment.START,
                    vertical_alignment = ft.CrossAxisAlignment.CENTER
                )
            ]
        )

        for i, cliente in enumerate(self.agendamentos, 1):
            self.agendados_prox.controls[1].controls.append(
                ft.Container(
                    col = 1,
                    padding = ft.Padding(left = 26, top = 26, right = 26,  bottom = 20),
                    bgcolor = c.fundo_neutralo,
                    border_radius = 34,
                    margin = ft.Margin(
                        left = vg.margin_left / 2 if i % 2 == 0 else vg.margin_left,
                        right = vg.margin_right /2 if i % 2 != 0 else vg.margin_right,
                    ),

                    shadow = c.shadow_leve(),

                    alignment = ft.Alignment.CENTER_LEFT,

                    content = ft.Column(
                        spacing = 0,
                        alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
                        horizontal_alignment = ft.CrossAxisAlignment.START,

                        controls = [
                            ft.Text(
                                value = self.agendamentos[cliente]['hora'],
                                size = 28, color = c.texto_secundario,
                                font_family = 'inter', weight = ft.FontWeight.W_300,
                                margin = ft.Margin(top = 8),
                            ),

                            ft.Text(
                                expand = True,
                                max_lines = 1,
                                overflow = ft.TextOverflow.ELLIPSIS,
                                margin = ft.Margin(top = 14),
                                value = f'{cliente}\n',
                                style = ft.TextStyle(
                                    size = 18, color = c.texto_secundario,
                                    font_family = 'inter', weight = ft.FontWeight.W_400
                                ),
                            ),
 
                            ft.Text(
                                expand = True,
                                max_lines = 1,
                                overflow = ft.TextOverflow.ELLIPSIS,
                                margin = ft.Margin(top = 6),
                                value = f'{self.agendamentos[cliente]['servico']}\n',
                                style = ft.TextStyle(
                                    size = 14, color = c.texto_secundario,
                                    font_family = 'inter', weight = ft.FontWeight.W_300
                                ),
                            ),
 
                            ft.Text(
                                expand = True,
                                max_lines = 1,
                                overflow = ft.TextOverflow.ELLIPSIS,
                                margin = ft.Margin(top = 6, bottom = 18),
                                value = f'{self.agendamentos[cliente]['setor']}\n',
                                style = ft.TextStyle(
                                    size = 14, color = c.texto_secundario,
                                    font_family = 'inter', weight = ft.FontWeight.W_300
                                ),
                            ),

                            ft.Stack(
                                width = 86,
                                height = 60,
                                margin = ft.Margin(right = 5),
                                alignment = ft.Alignment.CENTER,

                                controls = [
                                    ft.Container(
                                        left = 0,
                                        width = 45,
                                        height  = 45,
                                        border_radius = 45 / 2,
                                        bgcolor = c.borda_neutra,
                                        alignment = ft.Alignment.CENTER,
            
                                        content = ic.svg_icon(
                                            'telefone',
                                            size = 25, color = c.texto_secundario,
                                        )
                                    ),

                                    ft.Container(
                                        right = 0,
                                        padding = 3,
                                        border_radius = (45 + 3) / 2,
                                        bgcolor = c.fundo_neutralo,

                                        content = ft.Container(
                                            width = 45,
                                            height  = 45,
                                            border_radius = 45 / 2,
                                            bgcolor = c.cor_verde_clara,
                                            alignment = ft.Alignment.CENTER,
                                                            
                                            content = ic.svg_icon(
                                                'whatsapp_icon',
                                                size = 25, color = c.cor_verde,
                                            )
                                        )
                                    ),
                                ]
                            )
                        ]
                    )
                )
            )
            if i == 3:
                break

        area_page = ft.Column(
            spacing = 0,
            expand = True,
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.START,
            controls = [
                self.banner,
                self.ferramentas,
                self.agendados_prox,
            ]
        )

        return area_page