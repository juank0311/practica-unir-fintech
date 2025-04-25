import tkinter as tk
from tkinter import messagebox
import argparse

# Crear el parser y añadir los argumentos
parser = argparse.ArgumentParser()
parser.add_argument("--lang", choices=["es", "en"], default="es")

# Obtener los argumentos
args = parser.parse_args()

# Seleccionar el mensaje basado en el idioma
msg = {"es": "¡Hola! Bienvenid@ a la actividad grupal Pull requests en GitHub", 
       "en": "Hello! Welcome to the group activity: Pull requests on GitHub"}[args.lang]

# Crear una ventana oculta
ventana = tk.Tk()
ventana.withdraw()  # Oculta la ventana principal

# Mostrar un mensaje emergente
messagebox.showinfo("Saludo", msg)

# Para ejecutar en la consola ejecutar "python saludo_popup.py"
# Para ejecutarlo en ingles en la consola ejecutar "python saludo_popup.py --lang en"