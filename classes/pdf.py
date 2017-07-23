# coding: utf-8

from weasyprint import HTML, CSS

class PDF:
    """ Classe que converterá os dados da amortização em um arquivo pdf """
    def __init__(self, valores):
        self.tipo = valores["tipo"]
        self.periodos = valores["periodos"]
        self.prestacoes = valores["prestacoes"]
        self.juros = valores["juros"]
        self.amortizacao = valores["amortizacao"]
        self.saldos = valores["saldos"]
        self.total_prestacoes = valores["total_prestacoes"]
        self.total_juros = valores["total_juros"]
        self.total_amortizacao = valores["total_amortizacao"]
        self.arquivo = valores["arquivo"]
        self.diretorio = valores["diretorio"]

    def salvar_pdf(self):
        HTML(string=self.html).write_pdf(self.diretorio + '/' + self.arquivo + '.pdf')

    def gerar_linhas_planilha(self):
        for i in self.periodos:
            if i != 0:
                self.html += '<tr><td>{0}</td><td>{1:.2f}</td><td>{2:.2f}</td><td>{3:.2f}</td><td>' \
                             '{4:.2f}</td></tr>'.format(self.periodos[i],
                                                        self.prestacoes[i],
                                                        self.juros[i],
                                                        self.amortizacao[i],
                                                        self.saldos[i])
            else:
                self.html += '<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4:.2f}</td>' \
                             '</tr>'.format(self.periodos[i],
                                            self.prestacoes[i],
                                            self.juros[i],
                                            self.amortizacao[i],
                                            self.saldos[i])

        self.html += '</tbody><tfoot><td><strong>Total</strong></td><td><strong>{0:.2f}</strong></td>' \
                     '<td><strong>{1:.2f}</strong></td><td><strong>{2:.2f}</strong></td></tfoot>' \
                     '</table></body></html>'.format(self.total_prestacoes,
                                                     self.total_juros,
                                                     self.total_amortizacao)

    def gerar_pdf(self):
        """ Método para calcular e gerar o pdf """
        print(self.tipo)
        titulo = ""
        if self.tipo == "SAC":
            titulo = "Sistema de Amortização Constante (SAC)"
        elif self.tipo == "Americano":
            titulo = "Sistema Americano de Amortização"
        else:
            titulo = "Sistema de Amortização Price"

        self.html = '<!DOCTYPE html><html lang="en"><head><title></title><meta charset="UTF-8">' \
                    '<style>table { font-size: 12px; border-collapse: collapse;}th, td' \
                    '{border: 1px solid #ccc; padding: 10px;text-align: left;}tr:nth-child' \
                    '(even) {background-color : #eee;}tr:nth-child(odd) {background-color: ' \
                    '#fff;}</style> </head><body><table border="1"><thead><tr><th colspan="5">' \
                    + titulo + '</th></tr></thead><tbody><tr><td>' \
                    '<strong>Período </strong></td><td><strong>Prestação (R$)</strong></td><td>' \
                    '<strong>Juros (R$)</strong></td><td><strong>Amortização (R$)</strong></td>' \
                    '<td><strong>Saldo Devedor (R$)</strong></td></tr>'

        self.gerar_linhas_planilha()
        self.salvar_pdf()
