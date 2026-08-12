import flet_audio as fta
import flet as ft
from pathlib import Path

AUDIO = Path(__file__).parent
pasta = AUDIO / 'assets' / 'audio'

sons_dir = {
    'error': {
        'selecao': str('audio/som_error.wav')
    },

    'sucesso': {
        'venda': str('audio/venda_realizada.mp3')
    }
}

som = {}

async def system_sons(page: ft.Page):
    for play in sons_dir:
        for src in sons_dir[play]:
            son = fta.Audio(
                src = sons_dir[play][src],
                volume = 1.0,
                on_loaded = lambda e: print("ÁUDIO CARREGADO!"),
                data = {'som': str(Path(sons_dir[play][src]).name)}
            )

            print(son.data['som'])
            som[son.data['som']] = son

            page.services.append(son)
            print('servicos_page', page.services)