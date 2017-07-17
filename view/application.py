# coding: utf-8

from tkinter import *

class Application:
    """ Classe que renderiza toda a interface gráfica da aplicação """
    def __init__(self, master=None):
        self.root = Frame(master)

        self.fonte = ("Arial", "12")

        self.container_titulo(self.root, "Preencha os dados abaixo")
        self.montante = self.container_montante()
        self.juros = self.container_tx_juros()
        self.parcelas = self.container_qtd_parcelas()
        self.amortizacao = self.container_tipos_amort()
        self.container_botoes()

        self.root.pack()

    def container_titulo(self, pai, texto):
        """ Método para criar o container e widgets do título """
        self.titulo = Frame(pai)
        self.titulo["pady"] = 10
        self.titulo.pack()

        self.texto = Label(self.titulo,
                           text=texto)
        self.texto["font"] = ("Arial", "12", "bold")
        self.texto.pack()

    def container_montante(self):
        """ Método para criar o container e widgets do montante """
        self.montante = Frame(self.root)
        self.montante["padx"] = 50
        self.montante["pady"] = 10
        self.montante.pack()

        self.rotulo = Label(self.montante,
                            text="Valor do montante:",
                            font=self.fonte)
        self.rotulo.pack(side=LEFT)

        self.valor = Entry(self.montante,
                           font=self.fonte)
        self.valor.pack(side=RIGHT)

        return self.valor.get()

    def container_tx_juros(self):
        """ Método para criar o container e widgets das taxas de juros """
        self.tx_juros = Frame(self.root)
        self.tx_juros["padx"] = 50
        self.tx_juros["pady"] = 10
        self.tx_juros.pack()

        self.rotulo = Label(self.tx_juros,
                            text="Tx. de juros anual:",
                            font=self.fonte)
        self.rotulo.pack(side=LEFT)

        self.valor = Entry(self.tx_juros,
                           font=self.fonte)
        self.valor.pack(side=RIGHT)

        return self.valor.get()

    def container_qtd_parcelas(self):
        """ Método para criar o container e widgets da qtd. de parcelas """
        self.qtd_parcelas = Frame(self.root)
        self.qtd_parcelas["padx"] = 50
        self.qtd_parcelas["pady"] = 10
        self.qtd_parcelas.pack()

        self.rotulo = Label(self.qtd_parcelas,
                            text="Qtde. de parcelas:",
                            font=self.fonte)
        self.rotulo.pack(side=LEFT)

        self.valor = Entry(self.qtd_parcelas,
                           font=self.fonte)
        self.valor.pack(side=RIGHT)

        return self.valor.get()

    def container_tipos_amort(self):
        """ Método para criar o container e widgets para selecionar o tipo de amortização """
        self.tipos = ["SAC", "Price", "Americano"]

        self.tipo_amort = Frame(self.root)
        self.tipo_amort["padx"] = 50
        self.tipo_amort["pady"] = 10
        self.tipo_amort.pack()

        self.container_titulo(self.tipo_amort, "Selecione o tipo de amortização")

        self.lista = Listbox(self.tipo_amort,
                             height=3,
                             selectbackground="pink",
                             font=self.fonte,
                             selectmode=SINGLE)
        for tipo in self.tipos:
            self.lista.insert(END, tipo)
        self.lista.pack()

        return self.lista.curselection()

    def container_botoes(self):
        """ Método para criar o container e widgets do botão de sair e de gerar planilha"""
        self.botoes = Frame(self.root)
        self.botoes["pady"] = 30
        self.botoes.pack()

        self.sair = Button(self.botoes,
                           text="sair",
                           font=self.fonte,
                           width=5,
                           padx=10,
                           command=self.root.quit)
        self.sair.pack(side=LEFT)

        self.gerar = Button(self.botoes,
                            text="gerar",
                            font=self.fonte,
                            width=5,
                            padx=10,
                            command=lambda: self.show(self.montante,
                                                      self.juros,
                                                      self.parcelas,
                                                      self.amortizacao))
        self.gerar.pack(side=LEFT)

    def show(self, a, b, c, d):
        """ Método de teste para exibir os valores inseridos no formulário """
        print("{0}\n{1}\n{2}\n{3}".format(a, b, c, d))
    