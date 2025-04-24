import tkinter as tk
from tkinter import messagebox

# Crear una ventana oculta
ventana = tk.Tk()
ventana.withdraw()  # Oculta la ventana principal

# Mostrar un mensaje emergente
messagebox.showinfo("Saludo", "¡Hola! Bienvenid@ a la actividad grupal Pull requests en GitHub")

# Para ejecutar en la consola ejecutar "python saludo_popup.py"