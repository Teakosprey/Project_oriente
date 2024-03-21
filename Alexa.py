import speech_recognition as sr 
import pyttsx3 
from tkinter import *
from tkinter.filedialog import *
import os
import pywhatkit as py
import datetime
import webbrowser
import subprocess
from gmail import enviar_correo
from pymongo import MongoClient

#Conexión a mongodb
cadena_conexion = "mongodb+srv://Israel:GAPI.agentkennedy33I9@cluster0.vvbkumg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
cliente = MongoClient(cadena_conexion)
db = cliente["usuarios"]
collection = db["numeros"]

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
    talk("Alumno")
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
        # Pregunta al usuario a quién quiere enviar el mensaje
        talk('¿A quién le quieres enviar el mensaje?')
        nombre_usuario = listen()

        # Buscar usuario en MongoDB
        user_data = collection.find_one({nombre_usuario: {"$exists": True}})
        print(nombre_usuario)
        print(user_data)

        if user_data:
            numero = user_data[nombre_usuario]
            without_space = numero.replace(' ', '')
            print(without_space)

            talk('Deja tu recado:')
            massage = listen()
            print(massage)

            current_time = datetime.datetime.now()
            hour = current_time.hour
            minute = current_time.minute + 1

            py.sendwhatmsg('+52'+without_space, str(massage), hour, minute)

            talk('en un momento le enviare el mensaje')
        else:
            talk('No se encontró el número de teléfono para el usuario.')

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

def funcionalidades_B():
    talk("Docente")
    respuesta = listen()

    if "descargar" in respuesta:
        talk("Ingresando a drive")
        # El comando que quieres ejecutar es python seguido del nombre de tu archivo
        comando = ["python", "descargarArchivosDrive.py"]

        # Usamos subprocess para ejecutar el comando
        subprocess.run(comando)
        talk("archivo descargado")

    elif "correo" in respuesta:
        talk("Por favor, di el asunto del correo electrónico:")
        asunto = listen()
        talk("Por favor, di el mensaje del correo electrónico:")
        mensaje = listen()
        enviar_correo(asunto,mensaje)

        talk("correo enviado")
    else:
        talk("Lo siento no puedo realizar esa consulta aun")