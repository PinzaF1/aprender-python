# 03_bucles.py - Aprendiendo bucles en Python

# Los bucles permiten repetir acciones
# Bucle for para iterar sobre una lista
frutas = ["manzana", "banana", "cereza"]

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