# coding: utf-8

from weasyprint import HTML, CSS

class PDF:
    """ Classe que converterá os dados da amortização em um arquivo pdf """
    def __init__(self, valores):
        self._tipo = valores["tipo"]
        self._periodos = valores["periodos"]
        self._prestacoes = valores["prestacoes"]
        self._juros = valores["juros"]
        self._amortizacao = valores["amortizacao"]
        self._saldos = valores["saldos"]
        self._total_prestacoes = valores["total_prestacoes"]
        self._total_juros = valores["total_juros"]
        self._total_amortizacao = valores["total_amortizacao"]
        self._arquivo = valores["arquivo"]
        self._diretorio = valores["diretorio"]

    def _salvar_pdf(self):
        HTML(string=self._html).write_pdf(self._diretorio + '/' + self._arquivo + '.pdf')

    def _gerar_linhas_planilha(self):
        for i in self._periodos:
            if i != 0:
                self._html += '<tr><td>{0}</td><td>{1:.2f}</td><td>{2:.2f}</td><td>{3:.2f}</td><td>' \
                              '{4:.2f}</td></tr>'.format(self._periodos[i],
                                                         self._prestacoes[i],
                                                         self._juros[i],
                                                         self._amortizacao[i],
                                                         self._saldos[i])
            else:
                self._html += '<tr><td>{0}</td><td>{1}</td><td>{2}</td><td>{3}</td><td>{4:.2f}</td>' \
                              '</tr>'.format(self._periodos[i],
                                             self._prestacoes[i],
                                             self._juros[i],
                                             self._amortizacao[i],
                                             self._saldos[i])

        self._html += '</tbody><tfoot><td><strong>Total</strong></td><td><strong>{0:.2f}</strong></td>' \
                      '<td><strong>{1:.2f}</strong></td><td><strong>{2:.2f}</strong></td></tfoot>' \
                      '</table></body></html>'.format(self._total_prestacoes,
                                                      self._total_juros,
                                                      self._total_amortizacao)

    def gerar_pdf(self):
        """ Método para calcular e gerar o pdf """
        titulo = ""
        if self._tipo == "SAC":
            titulo = "Sistema de Amortização Constante (SAC)"
        elif self._tipo == "Americano":
            titulo = "Sistema Americano de Amortização"
        else:
            titulo = "Sistema de Amortização Price"

        self._html = '<!DOCTYPE html><html lang="en"><head><title></title><meta charset="UTF-8">' \
                     '<style>table { font-size: 12px; border-collapse: collapse;}th, td' \
                     '{border: 1px solid #ccc; padding: 10px;text-align: left;}tr:nth-child' \
                     '(even) {background-color : #eee;}tr:nth-child(odd) {background-color: ' \
                     '#fff;}</style> </head><body><table border="1"><thead><tr><th colspan="5">' \
                     + titulo + '</th></tr></thead><tbody><tr><td>' \
                     '<strong>Período </strong></td><td><strong>Prestação (R$)</strong></td><td>' \
                     '<strong>Juros (R$)</strong></td><td><strong>Amortização (R$)</strong></td>' \
                     '<td><strong>Saldo Devedor (R$)</strong></td></tr>'

        self._gerar_linhas_planilha()
        self._salvar_pdf()
