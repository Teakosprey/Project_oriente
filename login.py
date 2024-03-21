from tkinter import *
from tkinter import ttk
from Conexion import *

class VentanaLogin:
    def __init__(self, root, mostrar_ventana_menu):
        self.root = root
        self.root.title("Inicio de sesión")
        self.root.geometry("500x500")
        self.mostrar_ventana_menu = mostrar_ventana_menu

        self.opciones = ["Alumno", "Docente"]

        # Cargar la imagen de fondo
        try:
            self.fondo = PhotoImage(file="Imagenes/Login.png")
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
            self.fondo = None

        # Mostrar la imagen de fondo si se pudo cargar
        if self.fondo:
            self.fondo_imagen = Label(root, image=self.fondo)
            self.fondo_imagen.place(x=0, y=0, relwidth=1, relheight=1)

        #Mostrar los campos/etiquetas del menu
        self.matricula = Label(root, text="Matricula", font=("Times New Roman", 15, "bold"))
        self.matricula.place(x=230, y=110)
        self.contraseña = Label(root, text="Contraseña", font=("Times New Roman", 15, "bold"))
        self.contraseña.place(x=230, y=250-40)

        #Campos a rellenar
        self.texto_Matricula = Entry(root, width=29)
        self.texto_Matricula.place(x=230, y=100+50)
        self.texto_Password = Entry(root, width=29, show="*")
        self.texto_Password.place(x=230, y= 200+50)

        #ComboBox
        self.comboBox = ttk.Combobox(self.root, values=self.opciones)
        self.comboBox.set("Elije una opcion")
        self.comboBox.place(x=230, y=310)

        #Botones

        self.boton_inicio_sesion = Button(self.root, text="SignUp", cursor="hand2", bg = "White", width = 12, relief = "flat", 
                      font = ("Comic Sans MS", 12, "bold"), command=self.verificar_credenciales)
        self.boton_inicio_sesion.place(x=300, y=405)
        boton2 = Button(self.root, text="Exit", cursor="hand2", bg = "White", width = 12, relief = "flat", 
                        font = ("Comic Sans MS", 12, "bold"), command=self.salir)
        boton2.place(x=40, y=405)

    def getMatricula(self):
        return self.texto_Matricula.get()
    
    def getContraseña(self):
        return self.texto_Password.get()

    def getPerfil(self):
        return self.comboBox.get()
    
    def verificar_credenciales(self):

        matricula = self.getMatricula()
        contraseña = self.getContraseña()
        perfil = self.getPerfil()

        credenciales_correctas = sesion(matricula, contraseña, perfil)  

        if credenciales_correctas == "concedido":
            self.mostrar_ventana_menu()
        else:
            pass

    
    def salir(self):
        self.root.destroy()




if __name__ == "__main__":
    root = Tk()
    global app
    app = VentanaLogin(root, None)
    root.mainloop()

