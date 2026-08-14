import flet as ft
import asyncio

tela_anterior = None
tela_atual = None
tela_nova = None

tela_reserva1 = None
tela_reserva2 = None
tela_reserva3 = None

def mudar_page(
    page: ft.Page,
    anterior = None, atual = None, nova = None, e = None,
    reserva1 = None, reserva2 = None, reserva3 = None
):
    async def disparar(e = None):
        global tela_anterior, tela_atual, tela_nova
        global tela_reserva1, tela_reserva2, tela_reserva3

        tela_anterior = anterior if anterior != None else tela_anterior
        if tela_anterior == None: print('anterior é None')

        tela_atual = atual if atual != None else tela_atual
        if tela_atual == None: print('atual é None')

        tela_nova = nova if nova != None else tela_nova
        if tela_nova == None: print('nova é None')
        
        tela_reserva1 = reserva1 if reserva1 != None else tela_reserva1
        tela_reserva2 = reserva2 if reserva2 != None else tela_reserva2
        tela_reserva3 = reserva3 if reserva3 != None else tela_reserva3

        if tela_atual is not None and tela_nova is not None:
            conteudo = tela_nova

            page.data['area_build'].controls.clear()
            page.data['area_build'].controls.append(conteudo)
            page.update()
        else:
            print('Falta uma tela ai man')

    return disparar