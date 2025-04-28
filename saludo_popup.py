import tkinter as tk
from tkinter import messagebox
import argparse

# Crear el parser y añadir los argumentos
parser = argparse.ArgumentParser()
parser.add_argument("--lang", choices=["es", "en"], default="es")
parser.add_argument("--remove-duplicates", action="store_true", 
                    help="Si se usa, elimina palabras duplicadas de la lista antes de imprimirlas")

# Obtener los argumentos
args = parser.parse_args()

# Seleccionar el mensaje basado en el idioma
msg = {"es": "¡Hola! Bienvenid@ a la actividad grupal Pull requests en GitHub",
       "en": "Hello! Welcome to the group activity: Pull requests on GitHub"}[args.lang]

# Crear una función para ordenar una lista y eliminar duplicados si es necesario
def sort_list(word_list, remove_duplicates=False):
    if remove_duplicates:
        # Usar un conjunto para eliminar duplicados
        word_list = list(set(word_list))
    return sorted(word_list)

# Lista de palabras de ejemplo
word_list = ["python", "git", "github", "python", "pull", "requests", "git"]

# Aplicar la función según el argumento
sorted_list = sort_list(word_list, args.remove_duplicates)

# Mostrar la lista ordenada en la consola
print("Lista ordenada:", sorted_list)

# Crear una ventana oculta
ventana = tk.Tk()
ventana.withdraw()  # Oculta la ventana principal

# Mostrar un mensaje emergente
messagebox.showinfo("Saludo", msg)

# Para ejecutar en la consola:
# python saludo_popup.py --remove-duplicates
# Para ejecutarlo en inglés con eliminación de duplicados:
# python saludo_popup.py --lang en --remove-duplicates