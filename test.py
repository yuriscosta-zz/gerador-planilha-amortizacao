# coding: utf-8

import unittest
from classes.sac import SAC
from classes.price import Price
from classes.americano import Americano

class TesteAmortizacao(unittest.TestCase):
    """ 
        Classe de teste para testar os valores gerados nas 
        classes SAC, Price e Americano
    """
    def teste_sac(self):
        """ Método para testar a classe SAC """
        valor_entrada = {'montante': '120000',
                         'juros': '1',
                         'parcelas': '12',
                         'arquivo': 'teste',
                         'amortizacao': 'SAC',
                         'diretorio': '/home/yuri/Documentos'}

        valor_saida = {'amortizacao': ['', 10000.0, 10000.0,
                                       10000.0, 10000.0,
                                       10000.0, 10000.0,
                                       10000.0, 10000.0,
                                       10000.0, 10000.0,
                                       10000.0, 10000.0,
                                       10000.0],
                       'total_amortizacao': 120000.0,
                       'total_prestacoes': 127800.0,
                       'total_juros': 7800.0,
                       'arquivo': 'teste',
                       'periodos': [0, 1, 2, 3, 4, 5, 6, 7,
                                    8, 9, 10, 11, 12],
                       'tipo': 'SAC',
                       'prestacoes': ['', 11200.0, 11100.0,
                                      11000.0, 10900.0,
                                      10800.0, 10700.0,
                                      10600.0, 10500.0,
                                      10400.0, 10300.0,
                                      10200.0, 10100.0], 
                       'juros': ['', 1200.0, 1100.0, 1000.0,
                                 900.0, 800.0, 700.0, 600.0,
                                 500.0, 400.0, 300.0, 200.0,100.0],
                       'saldos': [120000.0, 110000.0, 100000.0,
                                  90000.0, 80000.0, 70000.0,
                                  60000.0, 50000.0, 40000.0,
                                  30000.0, 20000.0, 10000.0, 0.0],
                       'diretorio': '/home/yuri/Documentos'}

        self.assertEqual(SAC(valor_entrada).get_valores(), valor_saida)

    def teste_price(self):
        """ Método para testar a classe Price """
        valor_entrada = {'montante': '30000',
                         'juros': '1.5',
                         'parcelas': '12',
                         'arquivo': 'teste',
                         'amortizacao': 'Price',
                         'diretorio': '/home/yuri/Documentos'}

        valor_saida = {'saldos': [30000.0, 27699.600212813115,
                                  25364.694428818428, 22994.76505806382,
                                  20589.28674674789, 18147.726260762225,
                                  15669.542367486774, 13154.185715812191,
                                  10601.098714362488, 8009.715407891041,
                                  5379.4613518225215, 2709.7534849129743,
                                  -2.1600499167107046e-10],
                        'diretorio': '/home/yuri/Documentos',
                        'arquivo': 'teste',
                        'total_juros': 3004.797446242402,
                        'total_prestacoes': 33004.79744624262,
                        'prestacoes': ['', 2750.399787186885, 2750.399787186885,
                                       2750.399787186885, 2750.399787186885,
                                       2750.399787186885, 2750.399787186885,
                                       2750.399787186885, 2750.399787186885,
                                       2750.399787186885, 2750.399787186885,
                                       2750.399787186885, 2750.399787186885],
                        'total_amortizacao': 30000.000000000222,
                        'periodos': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                        'juros': ['', 450.0, 415.4940031921967, 380.4704164322764,
                                  344.92147587095724, 308.83930120121835,
                                  272.21589391143334, 235.0431355123016,
                                  197.31278573718285, 159.01648071543732,
                                  120.1457311183656, 80.69192027733781,
                                  40.646302273694616],
                        'tipo': 'Price',
                        'amortizacao': ['', 2300.399787186885, 2334.905783994688,
                                        2369.9293707546085, 2405.478311315928,
                                        2441.5604859856667,2478.1838932754517,
                                        2515.3566516745836, 2553.0870014497023,
                                        2591.3833064714477, 2630.2540560685193,
                                        2669.707866909547, 2709.7534849131903]}

        self.assertEqual(Price(valor_entrada).get_valores(), valor_saida)

    def teste_americano(self):
        """ Método para testar a classe Americano """
        valor_entrada = {'montante': '50000',
                         'juros': '3',
                         'parcelas': '10',
                         'arquivo': 'teste',
                         'amortizacao': 'Americano',
                         'diretorio': '/home/yuri/Documentos'}

        valor_saida = {'saldos': [50000.0, 50000.0, 50000.0, 50000.0,
                                  50000.0, 50000.0, 50000.0, 50000.0,
                                  50000.0, 50000.0, 0.0],
                       'arquivo': 'teste',
                       'amortizacao': ['', 0, 0, 0, 0, 0, 0, 0, 0, 0, 50000.0],
                       'total_amortizacao': 50000.0,
                       'periodos': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                       'total_juros': 15000.0,
                       'total_prestacoes': 65000.0,
                       'juros': ['', 1500.0, 1500.0, 1500.0, 1500.0, 1500.0,
                                 1500.0, 1500.0, 1500.0, 1500.0, 1500.0],
                       'diretorio': '/home/yuri/Documentos',
                       'prestacoes': ['', 1500.0, 1500.0, 1500.0, 1500.0,
                                      1500.0, 1500.0, 1500.0,
                                      1500.0, 1500.0, 51500.0],
                       'tipo': 'Americano'}

        self.assertEqual(Americano(valor_entrada).get_valores(), valor_saida)
        
if __name__ == '__main__':
	unittest.main()