# 05_funciones.py - Aprendiendo funciones en Python

# Las funciones permiten agrupar código reutilizable
def saludar(nombre):
    return f"Hola, {nombre}!"

def sumar(a, b):
    return a + b

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

# Usando las funciones
print(saludar("Carlos"))
print("2 + 3 =", sumar(2, 3))
print("¿Es mayor de 18 años? (25):", es_mayor_de_edad(25))
print("¿Es mayor de 18 años? (15):", es_mayor_de_edad(15))