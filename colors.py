import flet as ft

# Base
branco = '#FFFFFF'
bg = '#F8F8FC'
bg_alt = '#F9F9F9'
borda = '#E9E7EE'
cinza_fundo = '#E5E5E5'

# Texto e ícones
ico = '#2D2A3D'
txt = '#2D2A3D'
txt_sec = '#6B6478'
txt_fra = '#9C94A8'

# Verde
verde = '#22B77A'
verde_cl = '#C8FFE8'
verde_esc = '#1A8C5F'

# Vermelho
vermelho = '#E23D3D'
vermelho_fundo = '#FFE8EC'
vermelho_esc = '#5C0000'
alerta = '#F94449'

# Amarelo
amarelo = '#E0A94A'
amarelo_cl = '#F6D58D'

# Roxo
roxo = '#8A2BE2'
roxo_cl = '#B39EF5'
roxo_esc = '#4B0082'
roxo_suave = '#E6AFFF'

# Acessórios
laranja = '#FFB47D'
rosa = '#DE3163'
sombra = '#D8D8F8'

# Aliases compatíveis com o código antigo
background = bg
bordas = borda
cinza_claro = bg_alt
cinza_gelo = txt_fra
preto_icons = ico
preto_icons1 = ico
textos = txt
sub_textos = txt_sec
sub_texto_claro = txt_fra
verde_fundo = verde_cl
lilas = roxo
lilas_calmo = roxo_cl
lilas_ativos = roxo
azul_violeta = roxo_esc
vermelho_escuro = vermelho_esc
borda_erro_1 = alerta
vermelho_fundo_claro = vermelho_fundo
selecao = roxo_suave

# Gradientes
gradiente_banner = [roxo, roxo_esc]
gradiente_botoes = [roxo, roxo_esc]

def gradiente_top_bottom(colors):
    return ft.LinearGradient(
        begin = ft.Alignment.TOP_LEFT,
        end = ft.Alignment.BOTTOM_RIGHT,
        colors = colors,
    )

def gradiente_linear_normal(colors):
    return ft.LinearGradient(
        begin = ft.Alignment.TOP_CENTER,
        end = ft.Alignment.BOTTOM_CENTER,
        colors = colors,
    )

def gradiente_circular():
    return ft.RadialGradient(
        radius = 10,
        colors = [roxo, roxo_cl],
        stops = [0, 0.5, 1]
    )

def shadow_leve(x = 0, y = 4, blr = 6, opc = 0.2):
    return ft.BoxShadow(
        blur_radius = blr,
        offset = ft.Offset(x, y),
        color = ft.Colors.with_opacity(color = sombra, opacity = opc)
    )

def shadow_buttons():
    return ft.BoxShadow(
        blur_radius = 10,
        offset = ft.Offset(0, 4),
        color = ft.Colors.with_opacity(color = roxo_esc, opacity = 0.4)
    )