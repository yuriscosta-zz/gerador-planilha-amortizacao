# coding: utf-8

"""
    Arquivo responsável pela inicialização do sistema
"""

from tkinter import *
from classes.application import Application

ROOT = Tk()
Application(ROOT)
ROOT.mainloop()

