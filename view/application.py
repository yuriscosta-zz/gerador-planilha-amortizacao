# coding: utf-8

from tkinter import *
from tkinter import filedialog
from controller.controller import Controller

class Application:
    """ Classe que renderiza toda a interface gráfica da aplicação """
    def __init__(self, master=None):
        self._root = Frame(master)
        
        self._fonte = ("Arial", "12")

        self._container_titulo(self._root, "Preencha os dados abaixo")
        self._container_montante()
        self._container_tx_juros()
        self._container_qtd_parcelas()
        self._container_nome_arquivo()
        self._container_tipos_amort()
        self._container_botoes()

        self._root.pack()

    def _container_titulo(self, pai, texto):
        """ Método para criar o container e widgets do título """
        self._titulo = Frame(pai)
        self._titulo["pady"] = 10

        self._texto = Label(self._titulo,
                            text=texto)
        self._texto["font"] = ("Arial", "12", "bold")
        self._texto.pack()

        self._titulo.pack()

    def _container_montante(self):
        """ Método para criar o container e widgets do montante """
        self._montante = Frame(self._root)
        self._montante["padx"] = 50
        self._montante["pady"] = 10

        self._rotulo = Label(self._montante,
                             text="Valor do montante:",
                             font=self._fonte)
        self._rotulo.pack(side=LEFT)

        self._valor_montante = Entry(self._montante,
                                     font=self._fonte)
        self._valor_montante.pack(side=RIGHT)
        self._montante.pack()

    def _container_tx_juros(self):
        """ Método para criar o container e widgets das taxas de juros """
        self._tx_juros = Frame(self._root)
        self._tx_juros["padx"] = 50
        self._tx_juros["pady"] = 10

        self._rotulo = Label(self._tx_juros,
                             text="Tx. de juros anual:",
                             font=self._fonte)
        self._rotulo.pack(side=LEFT)

        self._valor_juros = Entry(self._tx_juros,
                                  font=self._fonte)
        self._valor_juros.pack(side=RIGHT)

        self._tx_juros.pack()

    def _container_qtd_parcelas(self):
        """ Método para criar o container e widgets da qtd. de parcelas """
        self._qtd_parcelas = Frame(self._root)
        self._qtd_parcelas["padx"] = 50
        self._qtd_parcelas["pady"] = 10

        self._rotulo = Label(self._qtd_parcelas,
                             text="Qtde. de parcelas:",
                             font=self._fonte)
        self._rotulo.pack(side=LEFT)

        self._valor_parcelas = Entry(self._qtd_parcelas,
                                     font=self._fonte)
        self._valor_parcelas.pack(side=RIGHT)

        self._qtd_parcelas.pack()

    def _container_tipos_amort(self):
        """ Método para criar o container e widgets para selecionar o tipo de amortização """
        self._tipos = ["SAC", "Price", "Americano"]

        self._tipo_amort = Frame(self._root)
        self._tipo_amort["padx"] = 50
        self._tipo_amort["pady"] = 10

        self._container_titulo(self._tipo_amort, "Selecione o tipo de amortização")

        self._lista = Listbox(self._tipo_amort,
                              height=3,
                              selectbackground="pink",
                              font=self._fonte,
                              selectmode=SINGLE)
        for tipo in self._tipos:
            self._lista.insert(END, tipo)
        self._lista.pack()

        self._tipo_amort.pack()

    def _container_nome_arquivo(self):
        """
            Método para criar o container e widgets para escolher um nome pro arquivo
            que será gerado
        """
        self._arquivo = Frame(self._root)

        self._rotulo = Label(self._arquivo,
                             text="Nome para o arquivo:",
                             font=self._fonte)
        self._rotulo.pack(side=LEFT)

        self._nome_arquivo = Entry(self._arquivo,
                                   font=self._fonte)
        self._nome_arquivo.pack(side=RIGHT)

        self._arquivo.pack()

    def _container_diretorio(self):
        """ Método para criar o container do buscador de diretórios """
        self._diretorio = Frame(self._root)
        self._diretorio["pady"] = 50
        self._diretorio["padx"] = 10

        self._local = filedialog.askdirectory(parent=self._diretorio,
                                              initialdir="/",
                                              title='Salvar em:')

        self._diretorio.pack()

    def _container_botoes(self):
        """ Método para criar o container e widgets do botão de sair e de gerar planilha"""
        self._botoes = Frame(self._root)
        self._botoes["pady"] = 30

        self._sair = Button(self._botoes,
                            text="sair",
                            font=self._fonte,
                            width=5,
                            padx=10,
                            command=self._root.quit)
        self._sair.pack(side=LEFT)

        self._gerar = Button(self._botoes,
                             text="gerar",
                             font=self._fonte,
                             width=5,
                             padx=10,
                             command=lambda: self._passar_dados(self._valor_montante.get(),
                                                                self._valor_juros.get(),
                                                                self._valor_parcelas.get(),
                                                                self._lista.get(self._lista.curselection()),
                                                                self._nome_arquivo.get()))
        self._gerar.pack(side=LEFT)

        self._botoes.pack()

    def _passar_dados(self, montante, juros, parcelas, amortizacao, arquivo):
        """ Método para enviar os valores para o controlador """
        self._container_diretorio()

        valores = {"montante":montante,
                   "juros":juros,
                   "parcelas":parcelas,
                   "amortizacao":amortizacao,
                   "arquivo":arquivo,
                   "diretorio":self._local}

        Controller(valores)

        self._container_titulo(self._root, "Salvo com sucesso!")
