# coding: utf-8

from weasyprint import HTML, CSS

class SAC:
    """ Classe que representa o Sistema de Amortização Constante """
    def __init__(self, valores):
        self.montante = int(valores["montante"])
        self.taxa_juros = float(valores["juros"])
        self.parcelas = int(valores["parcelas"])
        self.amortizacao = valores["amortizacao"]
        self.arquivo = valores["arquivo"]
        self.diretorio = valores["diretorio"]

        self.gerar_valores()

    def gerar_valores(self):
        """ Método para calcular e gerar os valores da tabela """
        self.lista_periodos = []
        self.lista_prestacao = ['']
        self.lista_juros = ['']
        self.lista_amortizacao = ['']
        self.lista_saldo_devedor = [self.montante]
        self.total_prestacao = 0
        self.total_juros = 0
        self.total_amortizacao = 0
        self.amortizacao = self.montante / self.parcelas
        self.lista_amortizacao.append(self.amortizacao)
        
        for i in range(0, self.parcelas+1):
            self.lista_periodos.append(i)
            if i != 0:             
                juros = self.taxa_juros * self.montante / 100
                prestacao = self.amortizacao + juros
                self.total_juros += juros
                self.total_prestacao += prestacao
                self.total_amortizacao += self.amortizacao
                self.montante -= self.amortizacao
                
                self.lista_prestacao.append(prestacao)
                self.lista_juros.append(juros)
                self.lista_amortizacao.append(self.amortizacao)
                self.lista_saldo_devedor.append(self.montante)

    def show(self):
        for i in range(self.parcelas+1):
            print("{0}\t{1}\t{2}\t{3}\t{4}".format(self.lista_periodos[i],
                                                   self.lista_prestacao[i],
                                                   self.lista_juros[i],
                                                   self.lista_amortizacao[i],
                                                   self.lista_saldo_devedor[i]))

        print("Total: {0}\t{1}\t{2}".format(self.total_prestacao,
                                            self.total_juros,
                                            self.total_amortizacao))

    def get_valores(self):
        valores = {"tipo": "SAC",
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
