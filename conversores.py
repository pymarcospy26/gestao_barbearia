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

        # valor_teste = '98594856376349332300045000.622'

        # vg.moeda_ativa = 'BR'
        # br = self.conversao_moeda(valor = valor_teste)
        # vg.moeda_ativa = 'ES'
        # es = self.conversao_moeda(valor = valor_teste)
        # vg.moeda_ativa = 'FR'
        # fr = self.conversao_moeda(valor = valor_teste)
        # vg.moeda_ativa = 'EUA'
        # eua = self.conversao_moeda(valor = valor_teste)

        # vg.moeda_ativa = 'BR'
        # br_d = self.conversao_moeda(p_decimal = br)
        # vg.moeda_ativa = 'ES'
        # es_d = self.conversao_moeda(p_decimal = es)
        # vg.moeda_ativa = 'FR'
        # fr_d = self.conversao_moeda(p_decimal = fr)
        # vg.moeda_ativa = 'EUA'
        # eua_d = self.conversao_moeda(p_decimal = eua)

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

    def conversao_moeda(self, valor = None, p_decimal = None, p_text = False):
        if valor == None and p_decimal == None: print('FALTA VALOR')
        else:
            valor_final = []
            if p_decimal == None:
                formatado = self.decimal_n(valor = valor, p_texto = True)
                quebra = str(formatado).split('.')
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


# Moedas()