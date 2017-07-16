# coding: utf-8

from weasyprint import HTML, CSS

class Price:
    """ Classe que representa a Tabela Price """
    def __init__(self, montante, taxa_juros, parcelas):
        self.montante = montante
        self.taxa_juros = taxa_juros
        self.parcelas = parcelas

    def gerar_tabela(self):
        """ Método para calcular e gerar a tabela """
        html = '<!DOCTYPE html><html lang="en"><head><title></title><meta charset="UTF-8">' \
               '<style>table { font-size: 12px; border-collapse: collapse;}th, td' \
               '{border: 1px solid #ccc; padding: 10px;text-align: left;}tr:nth-child' \
               '(even) {background-color : #eee;}tr:nth-child(odd) {background-color: ' \
               '#fff;}</style> </head><body><table border="1"><thead><tr><th colspan="5">' \
               'Sistema de Amortização Price</th></tr></thead><tbody><tr><td>' \
               '<strong>Período </strong></td><td><strong>Prestação (R$)</strong></td><td>' \
               '<strong>Juros (R$)</strong></td><td><strong>Armotização (R$)</strong></td>' \
               '<td><strong>Saldo Devedor (R$)</strong></td></tr>'

        taxa_unitaria = self.taxa_juros / 100
        amortizacao = 0
        total_prestacao = 0
        total_juros = 0
        total_amortizacao = 0
        prestacao = self.montante * (taxa_unitaria / (1 - (1 + taxa_unitaria)**-self.parcelas))
        for i in range(0, self.parcelas+1):
            if i != 0:
                juros = self.montante * taxa_unitaria
                amortizacao = prestacao - juros
                self.montante -= amortizacao
                total_juros += juros
                total_prestacao += prestacao
                total_amortizacao += amortizacao

                html += '<tr><td>{0}</td><td>{1:.2f}</td><td>{2:.2f}</td><td>{3:.2f}</td><td>' \
                        '{4:.2f}</td></tr>'.format(i, prestacao, juros, amortizacao, self.montante)
            else:
                html += '<tr><td>{0}</td><td></td><td></td><td></td><td>{1:.2f}</td>' \
                        '</tr>'.format(i, self.montante)

        html += '</tbody><tfoot><td><strong>Total</strong></td><td><strong>{0:.2f}</strong></td>' \
                '<td><strong>{1:.2f}</strong></td><td><strong>{2:.2f}</strong></td></tfoot>' \
                '</table></body></html>'.format(total_prestacao, total_juros, total_amortizacao)
        HTML(string=html).write_pdf('Price.pdf')

if __name__ == '__main__':
    x = Price(30000, 1.5, 12)
    x.gerar_tabela()
