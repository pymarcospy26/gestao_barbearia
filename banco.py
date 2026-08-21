import sqlite3
import asyncio
import flet as ft
from datetime import datetime
from decimal import Decimal
from pathlib import Path

BANCO = Path(__file__).resolve().parent
BANCO = BANCO / 'banco.db'

sqlite3.register_adapter(Decimal, str)

def servico_valor_base():
    con = sqlite3.connect(BANCO)
    cursor = con.cursor()

    cursor.execute('''SELECT setor, servico, valor FROM catalogo''')

    resultados_s_v = cursor.fetchall()
    con.close()

    return resultados_s_v

async def servico_valor():
    return await asyncio.to_thread(servico_valor_base)

def setores_base():
    con = sqlite3.connect(BANCO)
    cursor = con.cursor()

    cursor.execute('''SELECT DISTINCT setor FROM catalogo''')

    resultados_set = cursor.fetchall()
    con.close()

    return [setor[0] for setor in resultados_set]
print(setores_base())
async def setores():
    return await asyncio.to_thread(setores_base)

def registrar_atendimento(
    servicos,
    subtotal,
    descontos,
    adicionais,
    valor_total,
    taxa_operacao,

    pix,
    dinheiro,
    cartao_debito,
    cartao_credito,

    troco
):
    con = sqlite3.connect(BANCO)
    cursor = con.cursor()

    cursor.execute(
        '''INSERT INTO atendimentos_nova
        (data, servicos, subtotal, adicionais,
        descontos, taxas_operacao, valor_total,
        dinheiro, pix, cartao_debito, cartao_credito, troco)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''',
        (
            datetime.now().strftime('%d/%m/%Y - %H:%M'),
            servicos, subtotal, adicionais,
            descontos, taxa_operacao,
            valor_total, dinheiro,
            pix, cartao_debito,
            cartao_credito,
            troco
        )
    )

    con.commit()
    con.close()

    print('adicionado!')

def consultar_atendimentos():
    con = sqlite3.connect(BANCO)
    cursor = con.cursor()

    cursor.execute("""
        SELECT
            id,
            data,
            servicos,
            subtotal,
            adicionais,
            descontos,
            taxas_operacao,
            valor_total,
            dinheiro,
            pix,
            cartao_debito,
            cartao_credito,
            troco
        FROM atendimentos_nova
    """)

    resultados = cursor.fetchall()

    con.close()

    return resultados

def limpar_registros_atendimentos(e = None):
    con = sqlite3.connect(BANCO)
    cursor = con.cursor()

    cursor.execute('DELETE FROM atendimentos_nova')
    cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'atendimentos_nova'")

    con.commit()
    con.close()

def status_idioma_page(idioma = 'BR', option = ['0 - Pega', '1 - Altera']):
    con = sqlite3.connect(BANCO)
    cursor = con.cursor()

    if option == 0:
        cursor.execute(
            'SELECT idioma FROM idioma_page WHERE id = 1'
        )

        return cursor.fetchone()[0]

    elif option == 1 and idioma in ['EUA', 'BR', 'ES', 'FR']:
        cursor.execute(
            'UPDATE idioma_page SET idioma = ? WHERE id = 1', (idioma,)
        )

    con.commit()
    con.close()

def status_tema_page(tema = None, option = ['0 - Pega', '1 - Altera']):
    con = sqlite3.connect(BANCO)
    cursor = con.cursor()

    if option == 0:
        cursor.execute(
            'SELECT tema FROM status_page WHERE id = 1'
        )

        return cursor.fetchone()[0]

    elif option == 1 and tema in ['claro', 'escuro']:
        cursor.execute(
            'UPDATE status_page SET tema = ? WHERE id = 1', (tema,)
        )

    con.commit()
    con.close()