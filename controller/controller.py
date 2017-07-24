# coding: utf-8

import sys
from classes.sac import SAC
from classes.americano import Americano
from classes.price import Price
from classes.pdf import PDF

class Controller:
    """ Classe responsável por armazenar as informações inseridas no formulário """
    def __init__(self, valores):
        self._valores = valores
        self._verificar_amortizacao()

    def _verificar_amortizacao(self):
        """ 
            Método para verificar o tipo de amortização e passar os dados 
            para o gerador de pdf
        """
        try:
            if (float(self._valores["montante"]) > 0 and
                float(self._valores["juros"]) and
                int(self._valores["parcelas"]) > 0):
                if self._valores["amortizacao"] == "SAC":
                    valores = SAC(self._valores).get_valores()
                elif self._valores["amortizacao"] == "Americano":
                    valores = Americano(self._valores).get_valores()
                else:
                    valores = Price(self._valores).get_valores()
                PDF(valores).gerar_pdf()
            else:
                sys.exit("Insira valores válidos!")
            
        except Exception as e:
            sys.exit(e)
