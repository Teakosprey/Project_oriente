from tkinter import *
from tkinter import ttk
from Alexa import funcionalidades_B, funcionalidades_A

class VentanaLogin:
    def __init__(self, root, mostrar_ventana_menu, funcionalidades_A, funcionalidades_B):
        self.root = root
        self.root.title("Inicio de sesión")
        self.root.geometry("500x500")
        self.mostrar_ventana_menu = mostrar_ventana_menu
        self.funcionalidades_A = funcionalidades_A
        self.funcionalidades_B = funcionalidades_B

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

        # Aquí vinculas el evento '<<ComboboxSelected>>' a la función on_combobox_select
        self.comboBox.bind('<<ComboboxSelected>>', lambda event: self.verificar_credenciales())

        #Botones

        self.boton_inicio_sesion = Button(self.root, text="SignUp", cursor="hand2", bg = "White", width = 12, relief = "flat", 
                      font = ("Comic Sans MS", 12, "bold"), command=self.ir_a_menu, state=DISABLED)
        self.boton_inicio_sesion.place(x=300, y=405)
        boton2 = Button(self.root, text="Exit", cursor="hand2", bg = "White", width = 12, relief = "flat", 
                        font = ("Comic Sans MS", 12, "bold"), command=self.salir)
        boton2.place(x=40, y=405)

    def verificar_credenciales(self, event=None):
        # Aquí puedes obtener el valor seleccionado
        selected_option = self.comboBox.get()
        if selected_option == 'Docente':
            self.funcionalidades = self.funcionalidades_B
        elif selected_option == 'Alumno':
            self.funcionalidades = self.funcionalidades_A
        self.habilitar_boton()

    def ir_a_menu(self):
        self.mostrar_ventana_menu(self.funcionalidades)

    def habilitar_boton(self, event=None):
        self.boton_inicio_sesion.config(state=NORMAL)
    
    def salir(self):
        self.root.destroy()

if __name__ == "__main__":
    root = Tk()
    app = VentanaLogin(root,None, funcionalidades_A, funcionalidades_B)
    root.mainloop()