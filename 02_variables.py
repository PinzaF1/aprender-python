# 02_variables.py - Aprendiendo variables en Python

# Las variables almacenan datos que podemos usar después
nombre = "Carlos"
edad = 25
altura = 1.75
activo = True

# Imprimir las variables
print("Hola, mi nombre es", nombre)
print("Tengo", edad, "años")
print("Mido", altura, "metros")
print("¿Estoy activo?", activo)

# Cambiar el valor de una variable
edad = edad + 1
print("El próximo año tendré", edad, "años")

# Tipos de datos
numero_entero = 42
numero_flotante = 3.14
texto = "Python es increíble"
lista_numeros = [1, 2, 3, 4, 5]

print("\nTipos de datos:")
print(f"Entero: {numero_entero}, tipo: {type(numero_entero)}")
print(f"Flotante: {numero_flotante}, tipo: {type(numero_flotante)}")
print(f"Lista: {lista_numeros}")