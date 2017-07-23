# coding: utf-8

from tkinter import *
from tkinter import filedialog
from controller.controller import Controller

class Application:
    """ Classe que renderiza toda a interface gráfica da aplicação """
    def __init__(self, master=None):
        self.root = Frame(master)
        
        self.fonte = ("Arial", "12")

        self.container_titulo(self.root, "Preencha os dados abaixo")
        self.container_montante()
        self.container_tx_juros()
        self.container_qtd_parcelas()
        self.container_nome_arquivo()
        self.container_tipos_amort()
        self.container_botoes()

        self.root.pack()

    def container_titulo(self, pai, texto):
        """ Método para criar o container e widgets do título """
        self.titulo = Frame(pai)
        self.titulo["pady"] = 10

        self.texto = Label(self.titulo,
                           text=texto)
        self.texto["font"] = ("Arial", "12", "bold")
        self.texto.pack()

        self.titulo.pack()

    def container_montante(self):
        """ Método para criar o container e widgets do montante """
        self.montante = Frame(self.root)
        self.montante["padx"] = 50
        self.montante["pady"] = 10

        self.rotulo = Label(self.montante,
                            text="Valor do montante:",
                            font=self.fonte)
        self.rotulo.pack(side=LEFT)

        self.valor_montante = Entry(self.montante,
                                    font=self.fonte)
        self.valor_montante.pack(side=RIGHT)
        self.montante.pack()

    def container_tx_juros(self):
        """ Método para criar o container e widgets das taxas de juros """
        self.tx_juros = Frame(self.root)
        self.tx_juros["padx"] = 50
        self.tx_juros["pady"] = 10

        self.rotulo = Label(self.tx_juros,
                            text="Tx. de juros anual:",
                            font=self.fonte)
        self.rotulo.pack(side=LEFT)

        self.valor_juros = Entry(self.tx_juros,
                                 font=self.fonte)
        self.valor_juros.pack(side=RIGHT)

        self.tx_juros.pack()

    def container_qtd_parcelas(self):
        """ Método para criar o container e widgets da qtd. de parcelas """
        self.qtd_parcelas = Frame(self.root)
        self.qtd_parcelas["padx"] = 50
        self.qtd_parcelas["pady"] = 10

        self.rotulo = Label(self.qtd_parcelas,
                            text="Qtde. de parcelas:",
                            font=self.fonte)
        self.rotulo.pack(side=LEFT)

        self.valor_parcelas = Entry(self.qtd_parcelas,
                                    font=self.fonte)
        self.valor_parcelas.pack(side=RIGHT)

        self.qtd_parcelas.pack()

    def container_tipos_amort(self):
        """ Método para criar o container e widgets para selecionar o tipo de amortização """
        self.tipos = ["SAC", "Price", "Americano"]

        self.tipo_amort = Frame(self.root)
        self.tipo_amort["padx"] = 50
        self.tipo_amort["pady"] = 10

        self.container_titulo(self.tipo_amort, "Selecione o tipo de amortização")

        self.lista = Listbox(self.tipo_amort,
                             height=3,
                             selectbackground="pink",
                             font=self.fonte,
                             selectmode=SINGLE)
        for tipo in self.tipos:
            self.lista.insert(END, tipo)
        self.lista.pack()

        self.tipo_amort.pack()

    def container_nome_arquivo(self):
        """
            Método para criar o container e widgets para escolher um nome pro arquivo
            que será gerado
        """
        self.arquivo = Frame(self.root)

        self.rotulo = Label(self.arquivo,
                            text="Nome para o arquivo:",
                            font=self.fonte)
        self.rotulo.pack(side=LEFT)

        self.nome_arquivo = Entry(self.arquivo,
                                  font=self.fonte)
        self.nome_arquivo.pack(side=RIGHT)

        self.arquivo.pack()

    def container_diretorio(self):
        """ Método para criar o container do buscador de diretórios """
        self.diretorio = Frame(self.root)
        self.diretorio["pady"] = 50
        self.diretorio["padx"] = 10

        self.local = filedialog.askdirectory(parent=self.diretorio,
                                             initialdir="/",
                                             title='Salvar em:')

        self.diretorio.pack()

    def container_botoes(self):
        """ Método para criar o container e widgets do botão de sair e de gerar planilha"""
        self.botoes = Frame(self.root)
        self.botoes["pady"] = 30

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
                            command=lambda: self.passar_dados(self.valor_montante.get(),
                                                              self.valor_juros.get(),
                                                              self.valor_parcelas.get(),
                                                              self.lista.get(self.lista.curselection()),
                                                              self.nome_arquivo.get()))
        self.gerar.pack(side=LEFT)

        self.botoes.pack()

    def passar_dados(self, a, b, c, d, e):
        """ Método para enviar os valores para o controlador """
        self.container_diretorio()

        valores = {"montante":a,
                   "juros":b,
                   "parcelas":c,
                   "amortizacao":d,
                   "arquivo":e,
                   "diretorio":self.local}

        Controller(valores)

        self.container_titulo(self.root, "Salvo com sucesso!")
