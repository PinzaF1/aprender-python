# 05_funciones.py - Aprendiendo funciones en Python

# Las funciones permiten agrupar código reutilizable
def saludar(nombre):
    return f"Hola, {nombre}!"

def sumar(a, b):
    return a + b

def es_mayor_de_edad(edad):
    """Valida si una persona es mayor de edad de forma simplificada"""
    return edad >= 18

def calcular_descuento(precio, porcentaje_descuento):
    """Calcula el precio final con descuento aplicado"""
    descuento = precio * (porcentaje_descuento / 100)
    return precio - descuento

# Usando las funciones
print(saludar("Carlos"))
print("2 + 3 =", sumar(2, 3))
print("¿Es mayor de 18 años? (25):", es_mayor_de_edad(25))
print("¿Es mayor de 18 años? (15):", es_mayor_de_edad(15))
print("Precio con 20% descuento:", calcular_descuento(100, 20))