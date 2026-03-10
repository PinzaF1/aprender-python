# 06_listas.py - Trabajando con listas en Python

# Crear una lista
frutas = ["manzana", "banana", "cereza"]
print("Lista de frutas:", frutas)

# Acceder a elementos
print("Primera fruta:", frutas[0])
print("Última fruta:", frutas[-1])

# Agregar elementos
frutas.append("naranja")
print("Después de agregar naranja:", frutas)

# Insertar en una posición
frutas.insert(1, "pera")
print("Después de insertar pera:", frutas)

# Eliminar elementos
frutas.remove("banana")
print("Después de eliminar banana:", frutas)

# Longitud de la lista
print("Número de frutas:", len(frutas))

# Iterar sobre la lista
print("Frutas en la lista:")
for fruta in frutas:
    print("-", fruta)

# Listas anidadas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Matriz:", matriz)
print("Elemento en [1][2]:", matriz[1][2])