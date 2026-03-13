# 07_dicionarios.py - Trabajando con diccionarios en Python

# Crear un diccionario
persona = {
    "nombre": "Carlos",
    "edad": 25,
    "ciudad": "Madrid"
}
print("Diccionario de persona:", persona)

# Acceder a valores
print("Nombre:", persona["nombre"])
print("Edad:", persona["edad"])

# Agregar o modificar valores
persona["profesion"] = "Ingeniero"
persona["edad"] = 26
print("Diccionario actualizado:", persona)

# Eliminar un elemento
del persona["ciudad"]
print("Después de eliminar ciudad:", persona)

# Iterar sobre claves y valores
print("Claves y valores:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")

# Verificar si una clave existe
if "nombre" in persona:
    print("La clave 'nombre' existe")

# Longitud del diccionario
print("Número de elementos:", len(persona))