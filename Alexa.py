import speech_recognition as sr 
import pyttsx3 
from tkinter import *
from tkinter.filedialog import *
import os
import pywhatkit as py
import datetime
import webbrowser
import subprocess

def abrir_ventana_archivos():
    root = Tk()
    root.withdraw()  # Oculta la ventana principal

    archivos_seleccionados = askopenfilenames(
        title="Selecciona archivos",
        filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*"), ("Imagenes", ".JPG" and ".PNG")]
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
    rec = ""
    try:
        with sr.Microphone() as source:  # Agrega paréntesis aquí
            listener.adjust_for_ambient_noise(source, duration=5)
            talk("TE ESCUCHO")
            mic = listener.listen(source, timeout=5)
            rec = listener.recognize_google(mic, language="es-ES")  # Usa listener para reconocer el audio
            rec = rec.lower()
            
            if nombre in rec:
                rec = rec.replace(nombre, '')
            else:
                pass

    except Exception as e:
        print(f"Error: {e}")
    return rec


#funciones de alumno, como:acceder a materias, calificaciones, etc.
def funcionalidades_A():

    respuesta = listen()

    if "eliminar" in respuesta:
        talk("Cargando el gestor de archivos, favor de seleccionar archivos para eliminar")
        
        archivos = abrir_ventana_archivos()
    
        talk("Total de archivos ingresados: " + str(len(archivos)))
    
        if archivos:
            try:
                for a in archivos:
                    os.remove(a)
                talk("Se ha terminado de eliminar los archivos")
            except Exception:
                talk("Ha ocurrido un error")
        else:
            talk("No se ha seleccionado ningun archivo")

    elif "mensaje" in respuesta:
        
        numero = str(input("Ingresa el numero: "))
        hora = int(datetime.datetime.now().hour)
        minutos = int(datetime.datetime.now().minute+1)
        py.sendwhatmsg(phone_no=numero, message="Hola mundo", time_hour=hora, time_min=minutos)

    elif "calificaciones" in respuesta:
        #Ingresar link para acceso directo de las calificaciones
        talk("Ingresando a las calificaciones")
        webbrowser.open("https://sunischolar-uopzr.integralware.mx/axboletaparcial_uo.aspx?+LInxfNq+2kOF463XdigCz69jRGU0n0K7Xei9qWS++6Gu7iw8Kyy8W7Z5IavdZtuvx4yfqkdEilRqhmJd/4KsQ==")

    elif "octave" in respuesta:
        talk("Ingresando a octave")
        subprocess.Popen("C:\Program Files\GNU Octave\Octave-8.4.0\octave-launch.exe")

    elif "plataforma" in respuesta:
        talk("Ingresando a la plataforma")
        webbrowser.open("https://eva360.soyuo.mx/login/index.php")

    elif "horario" in respuesta:
        talk("Ingresando al horario")
        webbrowser.open("https://sunischolar-uopzr.integralware.mx/axhorarioalumno_std.aspx?g1DF4+wVbLAmXloUz/2KwtWAUFgPDk5ZQ+CyGAcum3Dbrv2ISjUSH5h1xoQ11QRL")

    elif "reproduce" in respuesta:
        musica = respuesta.replace("reproduce", "")
        py.playonyt(musica)

    elif "atlas" in respuesta:
        talk("Ingresando a MongoDB Atlas")
        webbrowser.open("https://www.mongodb.com/es/cloud/atlas/register")

    elif "base de datos" in respuesta:
        talk("Ingresando a MySQL")
        subprocess.Popen("C:/Program Files/MySQL/MySQL Workbench 8.0/MySQLWorkbench.exe")

    else:
        talk("Lo siento no puedo realizar esa consulta aun")

