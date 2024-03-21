from tkinter import *
# menu.py
class VentanaMenu:
    def __init__(self, root, mostrar_ventana_login, funcionalidades):
        self.root = root
        self.root.title("Menú Principal")
        self.root.geometry("500x500")
        self.mostrar_ventana_login = mostrar_ventana_login
        self.funcionalidades = funcionalidades

        # Cargar la imagen de fondo
        try:
            self.fondo = PhotoImage(file="Imagenes/Bienvenido.png")
        except Exception as ex:
            self.fondo = None

        # Mostrar la imagen de fondo si se pudo cargar
        if self.fondo:
            self.fondo_imagen = Label(self.root, image=self.fondo)
            self.fondo_imagen.place(x=0, y=0, relwidth=1, relheight=1)

        #Botones
        self.boton_virtual = Button(self.root, height=2, width=20, bg="Blue", text="ESCUCHAR", font=("Times New Roman", 15, "bold"), foreground= "White", command=self.funcionalidades)
        self.boton_virtual.place(x=95, y=375)

        self.boton_regresar = Button(self.root, height=1, width=5, text="Volver", font=("Comic Sans MS", 12, "bold"), bg="White", command=self.volver)
        self.boton_regresar.place(x=10, y=10)

    def volver(self):
        self.mostrar_ventana_login()    