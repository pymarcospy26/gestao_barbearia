import flet as ft
from decimal import Decimal
import variaveis_globais as vg

class Moedas:
    def __init__(self):
        self.moedas = {
            'BR': ['R$ 1.234,56', '.', ',', 0, 'R$ '],
            'ES': ['1.234,56 €', '.', ',', -1, ' €'],
            'FR': ['1 234,56 €', ' ', ',', -1, ' €'],
            'EUA': ['$ 1,234.56', ',', '.', 0, '$ '],
        }

        # valor_teste = '.9....95959595..303,,3,3,3,3  33.'

        # vg.moeda_ativa = 'BR'
        # br = self.conversao_moeda(valor = valor_teste)
        # if br is None: return
        # vg.moeda_ativa = 'ES'
        # es = self.conversao_moeda(valor = valor_teste)
        # if es is None: return
        # vg.moeda_ativa = 'FR'
        # fr = self.conversao_moeda(valor = valor_teste)
        # if fr is None: return
        # vg.moeda_ativa = 'EUA'
        # eua = self.conversao_moeda(valor = valor_teste)
        # if eua is None: return

        # vg.moeda_ativa = 'BR'
        # br_d = self.conversao_moeda(p_decimal = br)
        # if br_d is None: return
        # vg.moeda_ativa = 'ES'
        # es_d = self.conversao_moeda(p_decimal = es)
        # if es_d is None: return
        # vg.moeda_ativa = 'FR'
        # fr_d = self.conversao_moeda(p_decimal = fr)
        # if fr_d is None: return
        # vg.moeda_ativa = 'EUA'
        # eua_d = self.conversao_moeda(p_decimal = eua)
        # if eua_d is None: return

        # print(f'CONVERTIDO BR: {br}')
        # print(f'DESCONVERTIDO BR: {br_d}\n\n')

        # print(f'CONVERTIDO ES: {es}')
        # print(f'DESCONVERTIDO ES: {es_d}\n\n')

        # print(f'CONVERTIDO FR: {fr}')
        # print(f'DESCONVERTIDO FR: {fr_d}\n\n')

        # print(f'CONVERTIDO EUA: {eua}')
        # print(f'DESCONVERTIDO EUA: {eua_d}\n\n')

    def decimal_n(self, valor = None, p_texto = False):
            if valor == None: return
            else:
                try:
                    formatacao = Decimal(str(valor)).quantize(Decimal('0.01'))
                    if p_texto == False:
                        return formatacao
                    else:
                        formatacao = str(formatacao)
                        return formatacao

                except Exception as err: print('NÂO FOI POSSÍVEL CONVERTER DECIMAL.\nERRO:\n', err)

    def conversao_moeda(self, valor = None, p_decimal = None, p_text = False, cifrao = False):
        if valor == None and p_decimal == None: print('FALTA VALOR')
        else:
            valor_final = []
            if p_decimal == None:
                novo_valor = []
                possiveis = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                mudancas = 0

                for x in valor[::-1]:
                    if x not in possiveis and x not in [',', ' ', '.']:
                        print(f'O valor inserido "[ {x} ]" não é válido')
                        return None
                    
                    elif x not in possiveis:
                        quantidade_algarismos = 0

                        for y in novo_valor:
                            if y not in possiveis:
                                break

                            else:
                                quantidade_algarismos += 1

                        if quantidade_algarismos >= 3:
                            x = ''

                        elif quantidade_algarismos <= 2:
                            if mudancas == 0:
                                if quantidade_algarismos > 0:
                                    x = '.'
                                    mudancas = 1

                                else:
                                    x = ''

                            else:
                                x = ''

                    if x != '':
                        novo_valor.append(x)

                novo_valor = ''.join(novo_valor)
                novo_valor = novo_valor[::-1]
                if '.' not in novo_valor:
                    novo_valor = f'{novo_valor}.00'

                formatado = self.decimal_n(valor = novo_valor, p_texto = True)
                print('NOVO VALOR: ', novo_valor)
                print('FORMATADO: ', formatado)
                quebra = str(formatado).split('.')
                print('QUEBRA: ', quebra)
                valor_cheio = quebra[0]
                valor_decimal = quebra[1]
                contador = 0
                valor_cheio_formatado = [] #12345 // 543,21 // 12,345

                for x in valor_cheio[::-1]:
                    contador += 1

                    if contador == 4:
                        contador = 1
                        valor_cheio_formatado.append(self.moedas[vg.moeda_ativa][1]) #casa de milhar
                        valor_cheio_formatado.append(x)

                    else:
                        valor_cheio_formatado.append(x)

                valor_cheio_formatado = valor_cheio_formatado[::-1] #VALOR CHEIO FORMATADO
                valor_decimal = str(self.moedas[vg.moeda_ativa][2]) + str(valor_decimal)    #VALOR DECIMAL COM SEPARADOR

                for x in valor_cheio_formatado:
                    valor_final.append(x)

                for x in valor_decimal:
                    valor_final.append(x)

                if cifrao:
                    if self.moedas[vg.moeda_ativa][3] == 0:
                        valor_final.insert(0, self.moedas[vg.moeda_ativa][4])

                    else:
                        valor_final.append(self.moedas[vg.moeda_ativa][4])

                valor_final = ''.join(valor_final)

            else:
                desconversao = str(p_decimal).replace(self.moedas[vg.moeda_ativa][4], '')            #REMOVE O ID DA MOEDA '$, R$...'
                desconversao = str(desconversao).replace(self.moedas[vg.moeda_ativa][1], '')     #REMOVE OS SEPARADORES DE MILHAR
                desconversao = str(desconversao).replace(self.moedas[vg.moeda_ativa][2], '.')    #REMOVE O SEPARADOR DECIMAL

                try:
                    valor_final = self.decimal_n(valor = desconversao)

                except Exception as err:
                    print('Não possível DESCONVERTER o valor\nERRO:\n', err)

        if p_text:
            return str(valor_final)
        else:
            return valor_final


Moedas()