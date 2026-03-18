# 12_archivos.py - Aprendiendo a trabajar con archivos en Python

# Abrir un archivo para escribir (se crea si no existe)
with open("ejemplo.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Hola desde Python en un archivo!\n")

# Abrir el archivo para leer
with open("ejemplo.txt", "r", encoding="utf-8") as archivo:
    contenido = archivo.read()

print("Contenido del archivo:")
print(contenido)
