import pymongo
from tkinter import *
from tkinter import messagebox

def mostrar_ventana_emergente(mensaje):
    root = Tk()
    root.withdraw()  # Oculta la ventana principal

    # Muestra la ventana emergente con el mensaje
    messagebox.showinfo("Mensaje", mensaje)

#def registrar_campos(usuario, contraseña, perfil):
#    url = "mongodb+srv://Victor_Manuel_Hernandez_Luna:3taEX0JZ167J9H8k@atlascluster.yvqvurq.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"
#
#    cliente = pymongo.MongoClient(url)
#
#    db = cliente["project_db"]
#    coleccion = db["Registros"]
#
#    registro = {
#        "usuario" : usuario,
#        "contraseña" : contraseña,
#        "perfil" : perfil
#    }
#
#    try:
#        coleccion.insert_one(registro)
#        mostrar_ventana_emergente("Se ha registrado con exito")
#    except Exception:
#        mostrar_ventana_emergente("Hubo un error con el registro")


def sesion(usuario, contraseña, perfil):
    url = "mongodb+srv://Victor_Manuel_Hernandez_Luna:3taEX0JZ167J9H8k@atlascluster.yvqvurq.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"
    cliente = pymongo.MongoClient(url)

    db = cliente["project_db"]
    coleccion = db["Registros"]

    if coleccion.find_one({"usuario" : usuario, "contraseña" : contraseña, "perfil" : perfil}):
        mostrar_ventana_emergente("Haz iniciado sesion")
        return str("concedido")
    else:
        mostrar_ventana_emergente("Este usuario no se encuentra, verifica que no hayas escrito mal un campo")
        return str("denegado")



