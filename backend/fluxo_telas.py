import flet as ft
import asyncio

tela_anterior = None
tela_atual = None
tela_nova = None

tela_reserva1 = None
tela_reserva2 = None
tela_reserva3 = None

def mudar_page(               # <- não é mais 'async def', é uma função normal
    page: ft.Page,
    anterior = None, atual = None, nova = None,
    reserva1 = None, reserva2 = None, reserva3 = None
):
    async def executar(e = None):     # <- ENVELOPE NOVO: tudo de antes mora aqui dentro
        global tela_anterior, tela_atual, tela_nova
        global tela_reserva1, tela_reserva2, tela_reserva3

        tela_anterior = anterior
        tela_atual = atual
        tela_nova = nova

        tela_reserva1 = reserva1
        tela_reserva2 = reserva2
        tela_reserva3 = reserva3

        if tela_atual is not None and tela_nova is not None:
            conteudo = tela_nova

            # se 'nova' for uma classe de tela (tem método .tela()), busca o conteúdo dela agora
            if hasattr(conteudo, 'tela'):
                resultado = conteudo.tela()
                conteudo = await resultado if asyncio.iscoroutine(resultado) else resultado

            page.controls[0].content = conteudo
            page.update()

        else:
            print('Falta uma tela ai man')

    return executar    # <- devolve a função pronta pra ser clicada, não executa nada ainda