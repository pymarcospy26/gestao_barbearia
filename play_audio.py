import flet_audio as fta
import flet as ft
from pathlib import Path

AUDIO = Path(__file__).parent
pasta = AUDIO / 'assets' / 'audio'

sons_dir = {
    'error': {
        'selecao': str('audio/som_error.wav-1.0')
    },

    'sucesso': {
        'venda': str('audio/venda_realizada.mp3-1.0')
    },

    'pop': {
        'select': str('audio/pop_select.mp3-1.0'),
        'apagar': str('audio/tap_apagar.mp3-0.1')
    }
}

som = {}

async def system_sons(page: ft.Page, vol = 1.0):
    for play in sons_dir:
        for src in sons_dir[play]:
            partes = sons_dir[play][src].split('-')
            son = fta.Audio(
                src = partes[0],
                volume = float(partes[1]),
                on_loaded = lambda e: print("ÁUDIO CARREGADO!"),
                data = {'som': str(Path(partes[0]).name)}
            )

            print(son.data['som'])
            som[son.data['som']] = son

            page.services.append(son)
            print('servicos_page', page.services)