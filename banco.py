import sqlite3
import asyncio
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