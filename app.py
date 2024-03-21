# app.py
import tkinter as tk
from login import VentanaLogin
from menu import VentanaMenu
from Alexa import *
from tkinter.filedialog import *

class Aplicacion:
    def __init__(self, funcionalidades_A, funcionalidades_B):
        self.raiz = tk.Tk()
        self.raiz.title("Mi Aplicación")
        self.funcionalidades_A = funcionalidades_A
        self.funcionalidades_B = funcionalidades_B
        self.mostrar_ventana_login()

    def mostrar_ventana_login(self):
        self.ventana_login = VentanaLogin(self.raiz, self.mostrar_ventana_menu, self.funcionalidades_A, self.funcionalidades_B)

    def mostrar_ventana_menu(self, funcionalidades):
        # No destruyas la ventana principal aquí
        self.ventana_menu = VentanaMenu(self.raiz, self.mostrar_ventana_login, funcionalidades)  # Crea la ventana del menú principal

if __name__ == "__main__":
    app = Aplicacion(funcionalidades_A, funcionalidades_B)
    app.raiz.mainloop()

