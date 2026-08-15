import flet as ft
import colors as c
import icons as ic
import banco as bd
import variaveis_globais as vg
from backend import fluxo_telas as fx
import dicionario_idioma as dic

class Registro_Atendimentos:
    def __init__(self, page: ft.Page):
        self.page = page

    def tela(self):
        return self.lista()

    def lista(self):
        async def apagar_atualizar(e):
            bd.limpar_registros_atendimentos(e)
            tela_nova = Registro_Atendimentos(self.page).tela()
            await fx.mudar_page(self.page, atual = lista, nova = tela_nova)(e)
        dados = bd.consultar_atendimentos()
        lista = ft.Column(
            spacing = 0,
            expand = True,
            scroll = ft.ScrollMode.AUTO,
            alignment = ft.MainAxisAlignment.START,
            horizontal_alignment = ft.CrossAxisAlignment.START,
            margin = ft.Margin(left = vg.margin_left, right = vg.margin_right, top = vg.margin_top),
            controls = [
                ft.ResponsiveRow(
                    columns = 2,
                    alignment = ft.MainAxisAlignment.START,
                    vertical_alignment = ft.CrossAxisAlignment.CENTER,
                    controls = [
                        ft.Row(
                            col = 2,
                            alignment = ft.MainAxisAlignment.CENTER,
                            controls = [
                                ft.Container(
                                    width = 74,
                                    height = 74,
                                    border_radius = 28,
                                    bgcolor = c.cor_vermelho_fundo,
                                    shadow = c.shadow_leve(),
                                    alignment = ft.Alignment.CENTER,
                                    data = {'page': self.page},

                                    content = ic.svg_icon(
                                        'lixeira',
                                        size = 30, color = c.cor_rosa
                                    ),

                                    on_click = apagar_atualizar,
                                    ink = True
                                )
                            ]
                        )
                    ]
                )
            ]
        )

        if len(dados) == 0:
            lista.scroll = None
            lista.alignment = ft.MainAxisAlignment.START
            lista.horizontal_alignment = ft.CrossAxisAlignment.CENTER
            lista.controls.append(
                ft.Column(
                    expand = True,
                    alignment = ft.MainAxisAlignment.CENTER,
                    horizontal_alignment = ft.CrossAxisAlignment.CENTER,
                    controls = [
                        ft.Container(
                            height = 300,
                            bgcolor = c.fundo_neutralo,
                            border_radius = 34,
                            alignment = ft.Alignment.CENTER,
                            border = ft.Border.all(width = 1.6, color = c.cor_rosa),
                            content = ft.Text(
                                value = dic.palavras[dic.idioma_select]['registros']['sem_informacoes'],
                                size = 26, color = c.cor_rosa,
                                font_family = 'inter', weight = ft.FontWeight.BOLD
                            )
                        )
                    ]
                )
            )
        
        else:
            lista.scroll = ft.ScrollMode.AUTO
            lista.alignment = ft.MainAxisAlignment.START
            lista.horizontal_alignment = ft.CrossAxisAlignment.START

            for atendimento in dados:
                id_atnd = atendimento[0]
                data = atendimento[1]
                servicos = atendimento[2]
                subtotal = atendimento[3]
                adicionais = atendimento[4]
                descontos = atendimento[5]
                taxas_operacao = atendimento[6]
                valor_total = atendimento[7]
                dinheiro = atendimento[8]
                pix = atendimento[9]
                cartao_debito = atendimento[10]
                cartao_credito = atendimento[11]
                troco = atendimento[12]

                controles_atendimento = [
                    ft.Text(
                        value = f'Atendimento #{id_atnd}',
                        size = 22, color = c.texto_principal, font_family = 'inter',
                        weight = ft.FontWeight.W_500, margin = ft.Margin(top = 26)
                    ),

                    ft.Text(
                        value = f'Data e hora:\n{data}',
                        size = 16, color = c.texto_secundario, font_family = 'inter',
                        text_align = ft.TextAlign.LEFT, margin = ft.Margin(bottom = vg.margin_top)
                    ),
                ]

                servicos = servicos.split('/')
                for busca in servicos:
                    options = busca.split('#')
                    servico_ex = options[1].split(':')[1]
                    quantidade_ex = options[2].split(':')[1]
                    total_ex = options[3].split(':')[1]
                    box = ft.Text(
                        font_family = 'inter',
                        text_align = ft.TextAlign.LEFT,
                        spans = [
                            ft.TextSpan(
                                text = f'{servico_ex}\n',
                                style = ft.TextStyle(
                                    size = 16,
                                    color = c.texto_principal,
                                    font_family = 'inter',
                                    weight = ft.FontWeight.W_500,
                                )
                            ),

                            ft.TextSpan(
                                text = f'Quantidade: {quantidade_ex}',
                                style = ft.TextStyle(
                                    size = 16,
                                    color = c.texto_secundario,
                                    font_family = 'inter',
                                )
                            ),

                            ft.TextSpan(
                                text = f'Total: {total_ex}',
                                style = ft.TextStyle(
                                    size = 16,
                                    color = c.texto_secundario,
                                    font_family = 'inter',
                                )
                            ),
                        ]
                    )

                    controles_atendimento.append(box)

                subtotal = ft.Text(
                    value = f'Subtotal: {subtotal}',
                    size = 16, color = c.texto_secundario, font_family = 'inter',
                    text_align = ft.TextAlign.LEFT, margin = ft.Margin(bottom = vg.margin_top)
                )
                controles_atendimento.append(subtotal)

                valores = ft.ResponsiveRow(
                    spacing = 12,
                    run_spacing = 12,
                    alignment = ft.MainAxisAlignment.START,
                    vertical_alignment = ft.CrossAxisAlignment.START,
                    columns = 2,
                    controls = [
                            ft.Text(
                                col = 1,
                                value = f'Adicionais: {adicionais}',
                                size = 16,
                                color = c.texto_secundario,
                            font_family = 'inter',
                            text_align = ft.TextAlign.LEFT,
                        ),
                        ft.Text(
                            col = 1,
                            value = f'Descontos: {descontos}',
                            size = 16,
                            color = c.texto_secundario,
                            font_family = 'inter',
                            text_align = ft.TextAlign.LEFT,
                        ),
                        ft.Text(
                            col = 1,
                            value = f'Pix: {pix}',
                            size = 16,
                            color = c.texto_secundario,
                            font_family = 'inter',
                            text_align = ft.TextAlign.LEFT,
                        ),
                        ft.Text(
                            col = 1,
                            value = f'Dinheiro: {dinheiro}',
                            size = 16,
                            color = c.texto_secundario,
                            font_family = 'inter',
                            text_align = ft.TextAlign.LEFT,
                        ),
                        ft.Text(
                            col = 1,
                            value = f'C. Débito: {cartao_debito}',
                            size = 16,
                            color = c.texto_secundario,
                            font_family = 'inter',
                            text_align = ft.TextAlign.LEFT,
                        ),
                        ft.Text(
                            col = 1,
                            value = f'C. Crédito: {cartao_credito}',
                            size = 16,
                            color = c.texto_secundario,
                            font_family = 'inter',
                            text_align = ft.TextAlign.LEFT,
                        ),
                        ft.Text(
                            col = 2,
                            value = f'Taxas Op.: {taxas_operacao}',
                            size = 16,
                            color = c.texto_secundario,
                            font_family = 'inter',
                            text_align = ft.TextAlign.LEFT,
                        ),
                        ft.Text(
                            col = 1,
                            value = f'Total: {valor_total}',
                            size = 16,
                            color = c.texto_principal,
                            font_family = 'inter',
                            weight = ft.FontWeight.W_500,
                            text_align = ft.TextAlign.LEFT,
                        ),
                        ft.Text(
                            col = 1,
                            value = f'Troco: {troco}',
                            size = 16,
                            color = c.texto_secundario,
                            font_family = 'inter',
                            text_align = ft.TextAlign.LEFT,
                        ),
                    ]
                )
                controles_atendimento.append(valores)

                estrutura = ft.Column(
                    spacing = 0,
                    alignment = ft.MainAxisAlignment.CENTER,
                    horizontal_alignment = ft.CrossAxisAlignment.START,
                    controls = controles_atendimento
                )

                lista.controls.append(estrutura)

                divider = ft.Container(
                    height = 1.6,
                    expand = True,
                    bgcolor = c.borda,
                    margin = ft.Margin(top = vg.margin_top)
                )

                controles_atendimento.append(divider)

        return lista