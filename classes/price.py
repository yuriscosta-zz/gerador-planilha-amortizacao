# coding: utf-8

from weasyprint import HTML, CSS

class Price:
    """ Classe que representa a Tabela Price """
    def __init__(self, valores):
        self.montante = int(valores["montante"])
        self.taxa_juros = float(valores["juros"])
        self.parcelas = int(valores["parcelas"])
        self.amortizacao = valores["amortizacao"]
        self.arquivo = valores["arquivo"]
        self.diretorio = valores["diretorio"]
        self.gerar_tabela()

    def gerar_tabela(self):
        """ Método para calcular e gerar os valores da tabela """
        self.lista_periodos = []
        self.lista_prestacao = ['']
        self.lista_juros = ['']
        self.lista_amortizacao = ['']
        self.lista_saldo_devedor = [self.montante]
        self.amortizacao = 0
        self.total_prestacao = 0
        self.total_juros = 0
        self.total_amortizacao = 0
        self.lista_amortizacao.append(self.amortizacao)
        taxa_unitaria = self.taxa_juros / 100
        prestacao = self.montante * (taxa_unitaria / (1 - (1 + taxa_unitaria)**-self.parcelas))
        
        for i in range(0, self.parcelas+1):
            self.lista_periodos.append(i)
            if i != 0:
                juros = self.montante * taxa_unitaria
                self.amortizacao = prestacao - juros
                self.montante -= self.amortizacao
                self.total_juros += juros
                self.total_prestacao += prestacao
                self.total_amortizacao += self.amortizacao

                self.lista_prestacao.append(prestacao)
                self.lista_juros.append(juros)
                self.lista_amortizacao.append(self.amortizacao)
                self.lista_saldo_devedor.append(self.montante)

    def get_valores(self):
        """ Método para retornar os valores dentro de um dicionário """
        valores = {"tipo": "Price",
                   "periodos": self.lista_periodos,
                   "prestacoes": self.lista_prestacao,
                   "juros": self.lista_juros,
                   "amortizacao": self.lista_amortizacao,
                   "saldos": self.lista_saldo_devedor,
                   "total_prestacoes": self.total_prestacao,
                   "total_juros": self.total_juros,
                   "total_amortizacao": self.total_amortizacao,
                   "arquivo": self.arquivo,
                   "diretorio": self.diretorio}
        return valores
