# 03_bucles.py - Aprendiendo bucles en Python

# Los bucles permiten repetir acciones
# Bucle for para iterar sobre una lista
frutas = ["manzana", "banana", "cereza", "naranja"]

print("Mis frutas favoritas:")
for fruta in frutas:
    print("- " + fruta)

# Bucle while para repetir hasta una condición
contador = 1
print("\nContando hasta 5:")
while contador <= 5:
    print(contador)
    contador += 1

print("¡Fin del conteo!")

# For con range
print("\nNúmeros del 1 al 10:")
for num in range(1, 11):
    print(f"Número: {num}")

# For con enumerate
print("\nFrutas con índice:")
for indice, fruta in enumerate(frutas, 1):
    print(f"{indice}. {fruta}")