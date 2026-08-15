import flet as ft
import banco as bd
import asyncio

tema = bd.status_tema_page(option = 0)

cores = {
    'claro': {
        # Base
        'fundo': '#F8F8FC',
        'fundo_alternativo': '#F9F9F9',
        'fundo_neutralo': '#FFFFFF',
        'borda': '#E9E7EE',
        'borda_neutra': '#E5E5E5',

        # Texto e ícones
        'texto_principal': '#2D2A3D',
        'texto_secundario': '#6B6478',
        'texto_suave': '#9C94A8',

        # Cor Principal (Roxo)
        'cor_principal': '#8A2BE2',
        'cor_principal_clara': '#B39EF5',
        'cor_principal_escura': '#4B0082',
        'cor_principal_suave': '#E6AFFF',

        # Verde
        'cor_verde': '#22B77A',
        'cor_verde_clara': '#C8FFE8',
        'cor_verde_escura': '#1A8C5F',

        # Vermelho
        'cor_vermelho': '#E23D3D',
        'cor_vermelho_fundo': '#FFE8EC',
        'cor_vermelho_escura': '#5C0000',
        'cor_alerta': '#F94449',

        # Amarelo
        'cor_amarelo': '#E0A94A',
        'cor_amarelo_clara': '#F6D58D',

        # Acessórios
        'cor_laranja': '#FFB47D',
        'cor_rosa': '#DE3163',
        'cor_sombra': '#D8D8F8',
    },
    
    'escuro': {
        # Base
        'fundo': '#1A1A1E',
        'fundo_alternativo': '#252529',
        'fundo_neutralo': '#2D2D31',
        'borda': '#3D3D41',
        'borda_neutra': '#4A4A4E',

        # Texto e ícones
        'texto_principal': '#E8E8EC',
        'texto_secundario': '#B8B0C4',
        'texto_suave': '#7A7280',

        # Cor Principal (Roxo)
        'cor_principal': "#A13AF5",
        'cor_principal_clara': '#C77DFF',
        'cor_principal_escura': "#C77DFF",
        'cor_principal_suave': '#5A189A',

        # Verde
        'cor_verde': '#1FB580',
        'cor_verde_clara': "#084E3A",
        'cor_verde_escura': "#003B28",

        # Vermelho
        'cor_vermelho': '#E63946',
        'cor_vermelho_fundo': '#7A1D1D',
        'cor_vermelho_escura': '#3B0000',
        'cor_alerta': '#F94449',

        # Amarelo
        'cor_amarelo': '#F4A460',
        'cor_amarelo_clara': '#FFB347',

        # Acessórios
        'cor_laranja': '#FF8C42',
        'cor_rosa': '#FF6B9D',
        'cor_sombra': '#0A0A0F',
    }
}

# Carrega cores baseado no tema selecionado
_cores_ativas = cores[tema]

# Base
fundo = _cores_ativas['fundo']
fundo_alternativo = _cores_ativas['fundo_alternativo']
fundo_neutralo = _cores_ativas['fundo_neutralo']
borda = _cores_ativas['borda']
borda_neutra = _cores_ativas['borda_neutra']

# Texto e ícones
texto_principal = _cores_ativas['texto_principal']
texto_secundario = _cores_ativas['texto_secundario']
texto_suave = _cores_ativas['texto_suave']

# Cor Principal
cor_principal = _cores_ativas['cor_principal']
cor_principal_clara = _cores_ativas['cor_principal_clara']
cor_principal_escura = _cores_ativas['cor_principal_escura']
cor_principal_suave = _cores_ativas['cor_principal_suave']

# Verde
cor_verde = _cores_ativas['cor_verde']
cor_verde_clara = _cores_ativas['cor_verde_clara']
cor_verde_escura = _cores_ativas['cor_verde_escura']

# Vermelho
cor_vermelho = _cores_ativas['cor_vermelho']
cor_vermelho_fundo = _cores_ativas['cor_vermelho_fundo']
cor_vermelho_escura = _cores_ativas['cor_vermelho_escura']
cor_alerta = _cores_ativas['cor_alerta']

# Amarelo
cor_amarelo = _cores_ativas['cor_amarelo']
cor_amarelo_clara = _cores_ativas['cor_amarelo_clara']

# Acessórios
cor_laranja = _cores_ativas['cor_laranja']
cor_rosa = _cores_ativas['cor_rosa']
cor_sombra = _cores_ativas['cor_sombra']

# Gradientes
gradiente_banner = [cor_principal, cor_principal_escura]
gradiente_botoes = [cor_principal, cor_principal_escura]

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
        colors = [cor_principal, cor_principal_clara],
        stops = [0, 0.5, 1]
    )

def shadow_leve(x = 0, y = 4, blr = 6, opc = 0.2):
    return ft.BoxShadow(
        blur_radius = blr,
        offset = ft.Offset(x, y),
        color = ft.Colors.with_opacity(color = cor_sombra, opacity = opc)
    )

def shadow_buttons():
    return ft.BoxShadow(
        blur_radius = 10,
        offset = ft.Offset(0, 4),
        color = ft.Colors.with_opacity(color = cor_principal_escura, opacity = 0.4)
    )

async def carregar_tema():
    global fundo
    global fundo_alternativo
    global fundo_neutralo
    global borda
    global borda_neutra

    global texto_principal
    global texto_secundario
    global texto_suave

    global cor_principal
    global cor_principal_clara
    global cor_principal_escura
    global cor_principal_suave

    global cor_verde
    global cor_verde_clara
    global cor_verde_escura

    global cor_vermelho
    global cor_vermelho_fundo
    global cor_vermelho_escura
    global cor_alerta

    global cor_amarelo
    global cor_amarelo_clara

    global cor_laranja
    global cor_rosa
    global cor_sombra

    global gradiente_banner
    global gradiente_botoes

    await asyncio.sleep(0.3)

    _cores_ativas = cores[bd.status_tema_page(option = 0)]

    # Base
    fundo = _cores_ativas['fundo']
    fundo_alternativo = _cores_ativas['fundo_alternativo']
    fundo_neutralo = _cores_ativas['fundo_neutralo']
    borda = _cores_ativas['borda']
    borda_neutra = _cores_ativas['borda_neutra']

    # Texto e ícones
    texto_principal = _cores_ativas['texto_principal']
    texto_secundario = _cores_ativas['texto_secundario']
    texto_suave = _cores_ativas['texto_suave']

    # Cor principal
    cor_principal = _cores_ativas['cor_principal']
    cor_principal_clara = _cores_ativas['cor_principal_clara']
    cor_principal_escura = _cores_ativas['cor_principal_escura']
    cor_principal_suave = _cores_ativas['cor_principal_suave']

    # Verde
    cor_verde = _cores_ativas['cor_verde']
    cor_verde_clara = _cores_ativas['cor_verde_clara']
    cor_verde_escura = _cores_ativas['cor_verde_escura']

    # Vermelho
    cor_vermelho = _cores_ativas['cor_vermelho']
    cor_vermelho_fundo = _cores_ativas['cor_vermelho_fundo']
    cor_vermelho_escura = _cores_ativas['cor_vermelho_escura']
    cor_alerta = _cores_ativas['cor_alerta']

    # Amarelo
    cor_amarelo = _cores_ativas['cor_amarelo']
    cor_amarelo_clara = _cores_ativas['cor_amarelo_clara']

    # Acessórios
    cor_laranja = _cores_ativas['cor_laranja']
    cor_rosa = _cores_ativas['cor_rosa']
    cor_sombra = _cores_ativas['cor_sombra']

    # Gradientes
    gradiente_banner = [cor_principal, cor_principal_escura]
    gradiente_botoes = [cor_principal, cor_principal_escura]