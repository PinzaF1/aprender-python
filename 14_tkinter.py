"""Lección 14: Interfaces gráficas simples con Tkinter

Este archivo muestra cómo crear una ventana básica en Python usando Tkinter.
Tkinter viene incluido en la biblioteca estándar de Python.

Para ejecutar:
    python 14_tkinter.py

"""

import tkinter as tk


def on_button_click():
    nombre = entry_nombre.get().strip()
    if nombre:
        etiqueta_resultado.config(text=f"¡Hola, {nombre}!")
    else:
        etiqueta_resultado.config(text="Por favor escribe tu nombre.")


# --- Crear ventana principal ---
root = tk.Tk()
root.title("Ejemplo Tkinter")
root.geometry("320x180")
root.resizable(False, False)

# --- Widgets ---
etiqueta_instruccion = tk.Label(root, text="Escribe tu nombre:", font=("Segoe UI", 11))
etiqueta_instruccion.pack(pady=(20, 6))

entry_nombre = tk.Entry(root, width=30, font=("Segoe UI", 11))
entry_nombre.pack(pady=(0, 12))

boton_saludar = tk.Button(root, text="Saludar", command=on_button_click, font=("Segoe UI", 11))
boton_saludar.pack(pady=(0, 12))

etiqueta_resultado = tk.Label(root, text="", font=("Segoe UI", 11, "italic"))
etiqueta_resultado.pack(pady=(0, 12))

# --- Ejecutar loop de eventos ---
root.mainloop()
