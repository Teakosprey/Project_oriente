import speech_recognition as sr 
import pyttsx3 
from tkinter import *
from tkinter.filedialog import *
import os
import pywhatkit as py
import datetime
import urllib

def abrir_ventana_archivos():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal

    archivos_seleccionados = askopenfilenames(
        title="Selecciona archivos",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")]
    )

    root.destroy()  # Cierra la ventana después de la selección

    return archivos_seleccionados


listener = sr.Recognizer()

nombre = "oriente"
enginee = pyttsx3.init()
enginee.setProperty('rate', 135)
enginee.setProperty('voice', 'Es-es')
    

def talk(text):
    enginee.say(text)
    enginee.runAndWait()

 
def listen():
    try:
        with sr.Microphone() as source:  # Agrega paréntesis aquí
            listener.adjust_for_ambient_noise(source, duration=5)
            talk("TE ESCUCHO")
            mic = listener.listen(source, timeout=5)
            rec = listener.recognize_google(mic)  # Usa listener para reconocer el audio
            rec = rec.lower()
            
            if nombre in rec:
                rec = rec.replace(nombre, '')
            else:
                pass
                

    except Exception as e:
        print(f"Error: {e}")


#funciones de alumno, como:acceder a materias, calificaciones, etc.
def funcionalidades_A():

    respuesta = listen()

    if 'eliminar' in respuesta:
        talk("Cargando el gestor de archivos, favor de seleccionar archivos para eliminar")
        archivos = abrir_ventana_archivos()
    
        talk("Total de archivos ingresados: ", len(archivos))
    
        if archivos:
            print("Archivos seleccionados:")
            e = 1
            for file in archivos:
                os.remove(file)
                talk("archivo ", e , " eliminado")
                e += 1
            
            talk("Se ha terminado de eliminar los archivos")
        else:
            talk("No se ha seleccionado ningun archivo")

    elif 'mensaje' in respuesta:
        
        numero = str(input("Ingresa el numero: "))
        hora = int(datetime.datetime.now().hour)
        minutos = int(datetime.datetime.now().minute+1)
        py.sendwhatmsg(phone_no=numero, message="Hola mundo", time_hour=hora, time_min=minutos)
    elif 'calificaciones' in respuesta:
        print()
    else:
        talk("Lo sineto no puedo realizar esa consulta aun")


#funciones de el profesor: consultar materias que le corresponden, su horario, etc.
def funcionalidades_D():
    respuesta = listen()
    if 'eliminar' in respuesta:
        talk("eliminando archivos")
    elif 'mensaje' in respuesta:
        talk("enviando mensaje")
    elif 'horario' in respuesta:
        talk("Cargando el horario")
    elif 'materias' in respuesta:
        talk("Cargando materias")
    else:
        talk("Lo siento no puedo realizar esa consulta aun")

def decision(r):
    if r == 1:
        funcionalidades_A()
    elif r == 2:
        funcionalidades_D()
