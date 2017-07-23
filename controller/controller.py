# coding: utf-8

from classes.sac import SAC
from classes.americano import Americano
from classes.price import Price
from classes.pdf import PDF

class Controller:
    """ Classe responsável por armazenar as informações inseridas no formulário """
    def __init__(self, valores):
        self.valores = valores
        self.verificar_amortizacao()

    def show(self):
        print("{0}\n{1}\n{2}\n{3}\n{4}\n{5}".format(type(self.valores["montante"]),
                                                    type(self.valores["juros"]),
                                                    type(self.valores["parcelas"]),
                                                    type(self.valores["amortizacao"]),
                                                    type(self.valores["arquivo"]),
                                                    type(self.valores["diretorio"])))

    def verificar_amortizacao(self):
        """ 
            Método para verificar o tipo de amortização e passar os dados 
            para o gerador de pdf
        """
        if self.valores["amortizacao"] == "SAC":
            valores = SAC(self.valores).get_valores()
        elif self.valores["amortizacao"] == "Americano":
            valores = Americano(self.valores).get_valores()
        else:
            valores = Price(self.valores).get_valores()
        PDF(valores).gerar_pdf()
