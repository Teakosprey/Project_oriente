import speech_recognition as sr 
import pyttsx3 
from tkinter import *
from tkinter.filedialog import *
import os
import pywhatkit as py
import datetime
import webbrowser
import subprocess
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from login import *
import time
from Conexion import *


def sunischolar(eleccion):

    matricula = "92200235"
    contraseña = "A0TXTURDW8"
    Perfil = "Alumno"

    driver = webdriver.Chrome()
    url = "https://sunischolar-uopzr.integralware.mx/login.aspx?"
    driver.get(url)

    # Iniciar sesión
    username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "vUSUARIOCODIGO")))
    username.clear()
    username.send_keys(matricula)

    password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "vUSUARIOPSW")))
    password.clear()
    password.send_keys(contraseña)

    perfil = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "vPERFIL")))
    combobox = Select(perfil)
    combobox.select_by_visible_text(Perfil)


    cargar = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "BTNLOGIN")))

    # Hacer clic en el botón de iniciar sesión
    cargar.click()

    # Esperar a que la página se cargue completamente (puedes ajustar el tiempo según sea necesario)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "GXState")))

    if eleccion == 1:
        link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Boleta Parcial')]")))
    elif eleccion == 2:
        link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Horario')]")))
    
    driver.execute_script(link.get_attribute("onclick"))

    # Puedes agregar más acciones después de hacer clic en el enlace según tus necesidades

    # Esperar antes de cerrar el navegador (puedes ajustar el tiempo según sea necesario)
    time.sleep(1000)

    # Cerrar el navegador
    driver.quit()


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
        sunischolar(1)

    elif "octave" in respuesta:
        talk("Ingresando a Octave")
        subprocess.Popen("C:\Program Files\GNU Octave\Octave-8.4.0\octave-launch.exe")

    elif "plataforma" in respuesta:
        talk("Ingresando a la plataforma")
        webbrowser.open("https://eva360.soyuo.mx/login/index.php")

    elif "horario" in respuesta:
        talk("Ingresando al horario")
        sunischolar(2)

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

