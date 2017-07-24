# coding: utf-8

from weasyprint import HTML, CSS

class Americano:
    """ Classe que representa o Sistema Americano de Amortização """
    def __init__(self, valores):
        self._montante = float(valores["montante"])
        self._taxa_juros = float(valores["juros"])
        self._parcelas = int(valores["parcelas"])
        self._amortizacao = valores["amortizacao"]
        self._arquivo = valores["arquivo"]
        self._diretorio = valores["diretorio"]
        self._gerar_valores()

    def _gerar_valores(self):
        """ Método para calcular e gerar os valores da tabela """
        self._lista_periodos = []
        self._lista_prestacao = ['']
        self._lista_juros = ['']
        self._lista_amortizacao = ['']
        self._lista_saldo_devedor = [self._montante]
        self._amortizacao = 0
        self._total_prestacao = 0
        self._total_juros = 0
        self._total_amortizacao = 0
        juros = self._montante * self._taxa_juros / 100

        for i in range(0, self._parcelas+1):
            self._lista_periodos.append(i)

            if i != 0:
                if i != self._parcelas:
                    prestacao = juros
                else:
                    self._amortizacao = self._montante
                    prestacao = self._amortizacao + juros
                    self._montante -= self._amortizacao

                self._total_juros += juros
                self._total_prestacao += prestacao
                self._total_amortizacao += self._amortizacao

                self._lista_prestacao.append(prestacao)
                self._lista_juros.append(juros)
                self._lista_amortizacao.append(self._amortizacao)
                self._lista_saldo_devedor.append(self._montante)

    def get_valores(self):
        """ Método para retornar os valores dentro de um dicionário """
        valores = {"tipo": "Americano",
                   "periodos": self._lista_periodos,
                   "prestacoes": self._lista_prestacao,
                   "juros": self._lista_juros,
                   "amortizacao": self._lista_amortizacao,
                   "saldos": self._lista_saldo_devedor,
                   "total_prestacoes": self._total_prestacao,
                   "total_juros": self._total_juros,
                   "total_amortizacao": self._total_amortizacao,
                   "arquivo": self._arquivo,
                   "diretorio": self._diretorio}
        return valores
