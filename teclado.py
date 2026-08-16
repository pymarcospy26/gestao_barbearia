import flet as ft
import colors as c

variacoes_letras = {
    1: {
        'letra': {
            'letra_minuscula': 'q',
            'letra_maiuscula': 'Q',
        },
        'numero': '1',
        'outros': '!',
    },

    2: {
        'letra': {
            'letra_minuscula': 'w',
            'letra_maiuscula': 'W',
        },
        'numero': '2',
        'outros': '@',
    },

    3: {
        'letra': {
            'letra_minuscula': 'e',
            'letra_maiuscula': 'E',
            'caracteres': ['é', 'è', 'ê', 'ë'],
        },
        'numero': '3',
        'outros': '#',
    },

    4: {
        'letra': {
            'letra_minuscula': 'r',
            'letra_maiuscula': 'R',
        },
        'numero': '4',
        'outros': '$',
    },

    5: {
        'letra': {
            'letra_minuscula': 't',
            'letra_maiuscula': 'T',
        },
        'numero': '5',
        'outros': '%',
    },

    6: {
        'letra': {
            'letra_minuscula': 'y',
            'letra_maiuscula': 'Y',
            'caracteres': ['ý', 'ÿ'],
        },
        'numero': '6',
        'outros': '^',
    },

    7: {
        'letra': {
            'letra_minuscula': 'u',
            'letra_maiuscula': 'U',
            'caracteres': ['ú', 'ù', 'û', 'ü'],
        },
        'numero': '7',
        'outros': '&',
    },

    8: {
        'letra': {
            'letra_minuscula': 'i',
            'letra_maiuscula': 'I',
            'caracteres': ['í', 'ì', 'î', 'ï'],
        },
        'numero': '8',
        'outros': '*',
    },

    9: {
        'letra': {
            'letra_minuscula': 'o',
            'letra_maiuscula': 'O',
            'caracteres': ['ó', 'ò', 'ô', 'õ', 'ö'],
        },
        'numero': '9',
        'outros': '(',
    },

    10: {
        'letra': {
            'letra_minuscula': 'p',
            'letra_maiuscula': 'P',
        },
        'numero': '0',
        'outros': ')',
    },


    11: {
        'letra': {
            'letra_minuscula': 'a',
            'letra_maiuscula': 'A',
            'caracteres': ['á', 'à', 'â', 'ã', 'ä'],
        },
        'numero': '-',
        'outros': '_',
    },

    12: {
        'letra': {
            'letra_minuscula': 's',
            'letra_maiuscula': 'S',
        },
        'numero': '/',
        'outros': '\\',
    },

    13: {
        'letra': {
            'letra_minuscula': 'd',
            'letra_maiuscula': 'D',
        },
        'numero': ':',
        'outros': ';',
    },

    14: {
        'letra': {
            'letra_minuscula': 'f',
            'letra_maiuscula': 'F',
        },
        'numero': ';',
        'outros': ':',
    },

    15: {
        'letra': {
            'letra_minuscula': 'g',
            'letra_maiuscula': 'G',
        },
        'numero': '(',
        'outros': '[',
    },

    16: {
        'letra': {
            'letra_minuscula': 'h',
            'letra_maiuscula': 'H',
        },
        'numero': ')',
        'outros': ']',
    },

    17: {
        'letra': {
            'letra_minuscula': 'j',
            'letra_maiuscula': 'J',
        },
        'numero': '€',
        'outros': '{',
    },

    18: {
        'letra': {
            'letra_minuscula': 'k',
            'letra_maiuscula': 'K',
        },
        'numero': '.',
        'outros': '}',
    },

    19: {
        'letra': {
            'letra_minuscula': 'l',
            'letra_maiuscula': 'L',
        },
        'numero': ',',
        'outros': '|',
    },


    20: {
        'letra': {
            'letra_minuscula': 'z',
            'letra_maiuscula': 'Z',
        },
        'numero': '!',
        'outros': '~',
    },

    21: {
        'letra': {
            'letra_minuscula': 'x',
            'letra_maiuscula': 'X',
        },
        'numero': '?',
        'outros': '`',
    },

    22: {
        'letra': {
            'letra_minuscula': 'c',
            'letra_maiuscula': 'C',
            'caracteres': ['ç'],
        },
        'numero': '@',
        'outros': '<',
    },

    23: {
        'letra': {
            'letra_minuscula': 'v',
            'letra_maiuscula': 'V',
        },
        'numero': '#',
        'outros': '>',
    },

    24: {
        'letra': {
            'letra_minuscula': 'b',
            'letra_maiuscula': 'B',
        },
        'numero': '$',
        'outros': '…',
    },

    25: {
        'letra': {
            'letra_minuscula': 'n',
            'letra_maiuscula': 'N',
            'caracteres': ['ñ'],
        },
        'numero': '%',
        'outros': '•',
    },

    26: {
        'letra': {
            'letra_minuscula': 'm',
            'letra_maiuscula': 'M',
        },
        'numero': '&',
        'outros': '=',
    },
}

def teclado_completo(page: ft.Page, campo):
    def devolver_letra(e):
        tecla = e.control.content.value
        campo.value = str(campo.value) + str(tecla)
    def tecla_variacao(letra_variacao):
        tecla_v = ft.Container(
            width = 58,
            expand = 1,
            height = 58,
            border_radius = 22,
            shadow = c.shadow_leve(),
            bgcolor = c.fundo_neutralo,
            content = ft.Text(
                value = letra_variacao,
                size = 16, color = c.texto_principal,
                font_family = 'inter'
            ),
        )

        return tecla_v
    def tecla_normal(letra):   
        tecla = ft.Container(
            expand = 1,
            border_radius = 12,
            shadow = c.shadow_leve(),
            bgcolor = c.fundo_neutralo,

            content = ft.Text(
                value = letra,
                size = 22, color = c.texto_principal,
                font_family = 'inter'
            ),

            width = (page.width - (4 * 11)) / 10,
            height = (page.height * 5 / 11) / 4,

            alignment = ft.Alignment.CENTER,

            ink = True,
            on_click = devolver_letra
        )

        return tecla
    def teclado_page():
        teclado = ft.Container(
            left = 0,
            right = 0,
            bottom = 0,
            width = page.width,
            height = page.height * 4 / 11,
            shadow = c.shadow_leve(y = -4),
            bgcolor = c.fundo_teclado,
            content = ft.Column(
                spacing = 4,
                alignment = ft.MainAxisAlignment.END,
                horizontal_alignment = ft.CrossAxisAlignment.CENTER
            ),
            padding = ft.Padding(top = 8, left = 4, right = 4, bottom = 12),
        )

        return teclado

    row_variacoes = ft.Row(
        spacing = 4,
        alignment = ft.MainAxisAlignment.CENTER,
        vertical_alignment = ft.CrossAxisAlignment.CENTER
    )
    box_variacao = ft.Container(
        height = 84,
        border_radius = 24,
        shadow = c.shadow_leve(),
        bgcolor = c.fundo_neutralo,
        content = row_variacoes
    )

    largura_teclas = (page.width - (4 * 11)) / 10

    espaco_entre_teclas_LATERAL = 4
    row_1 = ft.Row(
        height = 80,
        spacing = espaco_entre_teclas_LATERAL,
        alignment = ft.MainAxisAlignment.CENTER,
        vertical_alignment = ft.CrossAxisAlignment.CENTER,
    )
    row_2 = ft.Row(
        height = 80,
        spacing = espaco_entre_teclas_LATERAL,
        alignment = ft.MainAxisAlignment.CENTER,
        vertical_alignment = ft.CrossAxisAlignment.CENTER,
    )
    row_3 = ft.Row(
        height = 80,
        spacing = espaco_entre_teclas_LATERAL,
        alignment = ft.MainAxisAlignment.CENTER,
        vertical_alignment = ft.CrossAxisAlignment.CENTER,
    )
    row_4 = ft.Row(
        height = 80,
        spacing = espaco_entre_teclas_LATERAL,
        alignment = ft.MainAxisAlignment.CENTER,
        vertical_alignment = ft.CrossAxisAlignment.CENTER,
    )

#===============TECLADO DE LETRAS===============

    for i, posicao in enumerate(variacoes_letras, 1):
        variacoes = variacoes_letras[posicao]['letra'].get('caracteres', [])
        letra_minuscula = variacoes_letras[posicao]['letra']['letra_minuscula']
        letra_maiuscula = variacoes_letras[posicao]['letra']['letra_maiuscula']

        if len(variacoes) > 0:
            for x in variacoes:
                row_variacoes.controls.append(tecla_variacao(x)) #adiciona as letras variantes da original

        if i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            row_1.controls.append(tecla_normal(letra_minuscula))

        if i in [11, 12, 13, 14, 15, 16, 17, 18, 19]:
            row_2.controls.append(tecla_normal(letra_minuscula))

        if i in [20, 21, 22, 23, 24, 25, 26]:
            row_3.controls.append(tecla_normal(letra_minuscula))

    row_4.controls.append(
        ft.Container(
            width = page.width / 2,
            bgcolor = c.cor_verde_clara,
            alignment = ft.Alignment.CENTER,
            height = (page.height * 5 / 11) / 4,
            content = ft.Text('espaço', size = 16, color = c.texto_principal),
        )
    )

    row_2.controls.insert(0, ft.Row(width = largura_teclas / 2))
    row_2.controls.append(ft.Row(width = largura_teclas / 2))

    row_3.controls.insert(
        0,
        ft.Container(
            border_radius = 12,
            bgcolor = c.cor_principal_escura,
            width = (largura_teclas * 3) / 2,
            height = (page.height * 5 / 11) / 4,
            alignment = ft.Alignment.CENTER,

            content = ft.Icon(
                icon = ft.CupertinoIcons.ARROW_UP,
                size = 22,
                color = c.fundo_neutralo
            )
        )
    )
    row_3.controls.append(
        ft.Container(
            border_radius = 12,
            bgcolor = c.cor_principal_escura,
            width = (largura_teclas * 3) / 2,
            height = (page.height * 5 / 11) / 4,
            alignment = ft.Alignment.CENTER,

            content = ft.Icon(
                icon = ft.CupertinoIcons.ARROW_LEFT,
                size = 22,
                color = c.fundo_neutralo
            )
        )
    )

    teclado_page_1 = teclado_page()
    teclado_page_1.content.controls.extend([
        row_1,
        row_2,
        row_3,
        row_4
    ])

    return teclado_page_1
        



