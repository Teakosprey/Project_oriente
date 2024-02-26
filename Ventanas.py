from tkinter import *
from tkinter import ttk
from tkinter.filedialog import *
from Alexa import *
from Conexion import *
    

#Mover y cerrar ventanas==================================================================================================================
def cambiar_asistente():
    ventana.destroy()
    ventana_Asistente()


#Cierra la ventana actual
def salir():
    ventana.destroy()

def volver():
    ventana2.destroy()
    Login()



#Interfazes===============================================================================================================================

def Login():

    opciones = ["Alumnos", "Docentes"]

    global ventana
    ventana = Tk()
    ventana.title("Inicio de sesion") #Titulo de la ventana
    ventana.geometry("500x500")
    try:
        fondo = PhotoImage(file="C:/Users/vmhl0/Escritorio/Proyecto/Imagenes/Login.png")
    except Exception as e:
        print(f"Error al cargar la imagen: {e}")
        fondo = None  # Evita problemas si la carga de la imagen falla
    # Mostrar la imagen de fondo si se pudo cargar
    if fondo:
        fondo_label = Label(ventana, image=fondo)
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    #Labels
    matricula = Label(ventana, text="Matricula", font=("Times New Roman", 15, "bold"))
    matricula.place(x=230, y=110)
    contraseña = Label(ventana, text="Contraseña", font=("Times New Roman", 15, "bold"))
    contraseña.place(x=230, y=250-40)

    #Text Field
    global Texto_Matricula
    global Texto_Password

    Texto_Matricula = Entry(ventana, width=29)
    Texto_Matricula.place(x=230, y=100+50)
    Texto_Password = Entry(ventana, width=29, show="*")
    Texto_Password.place(x=230, y= 200+50)

    #Botones
    global boton

    boton = Button(ventana, text="SignUp", cursor="hand2", bg = "White", width = 12, relief = "flat", 
                      font = ("Comic Sans MS", 12, "bold"), command=cambiar_asistente)
    boton.place(x=300, y=405)
    boton2 = Button(ventana, text="Exit", cursor="hand2", bg = "White", width = 12, relief = "flat", 
                      font = ("Comic Sans MS", 12, "bold"), command=salir)
    boton2.place(x=40, y=405)

    #ComboBox
    global comboBox

    comboBox = ttk.Combobox(ventana, values=opciones)
    comboBox.set("Elije una opcion")
    comboBox.place(x=230, y=310)

    ventana.mainloop()




def ventana_Asistente():

    global ventana2
    ventana2 = Tk()
    ventana2.title("Asistente Virtual")
    ventana2.geometry("500x500")

    try:
        fondo = PhotoImage(file="C:/Users/vmhl0/Escritorio/Proyecto/Imagenes/Bienvenido.png")
    except Exception as ex:
        fondo = None

    if fondo:
        fondo_label = Label(ventana2, image=fondo)
        fondo_label.place(x=0, y=0, relwidth=1, relheight=1)

    boton_virtual = Button(ventana2, height=2, width=20, bg="Blue", text="ESCUCHAR", font=("Times New Roman", 15, "bold"), foreground= "White", command=funcionalidades_A)
    boton_virtual.place(x=133, y=375)

    boton_regresar = Button(ventana2, height=1, width=5, text="Volver", font=("Comic Sans MS", 12, "bold"), bg="White", command=volver)
    boton_regresar.place(x=10, y=10)    

    ventana2.mainloop()

Login()
