# 08_tuplas.py - Trabajando con tuplas en Python

# Las tuplas son secuencias inmutables de elementos
# Se crean con paréntesis ()
tupla_vacia = ()
tupla_un_elemento = (1,)  # Nota: la coma es necesaria para un solo elemento
tupla_numeros = (1, 2, 3, 4, 5)
tupla_mixta = ("Hola", 42, True, 3.14)

print("Tupla vacía:", tupla_vacia)
print("Tupla con un elemento:", tupla_un_elemento)
print("Tupla de números:", tupla_numeros)
print("Tupla mixta:", tupla_mixta)

# Acceder a elementos por índice
print("Primer elemento:", tupla_numeros[0])
print("Último elemento:", tupla_numeros[-1])

# Las tuplas son inmutables - no se pueden modificar
# Esto daría error: tupla_numeros[0] = 10

# Operaciones con tuplas
print("Longitud de la tupla:", len(tupla_numeros))
print("Máximo valor:", max(tupla_numeros))
print("Mínimo valor:", min(tupla_numeros))

# Concatenar tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print("Tupla concatenada:", tupla_concatenada)

# Repetir tupla
tupla_repetida = tupla1 * 3
print("Tupla repetida:", tupla_repetida)

# Verificar si un elemento está en la tupla
print("¿Está 3 en tupla_numeros?", 3 in tupla_numeros)

# Iterar sobre una tupla
print("Elementos de la tupla:")
for elemento in tupla_numeros:
    print(elemento)

# Desempaquetado de tuplas
a, b, c, d, e = tupla_numeros
print(f"Desempaquetado: a={a}, b={b}, c={c}, d={d}, e={e}")

# Tuplas anidadas
tupla_anidada = ((1, 2), (3, 4), (5, 6))
print("Tupla anidada:", tupla_anidada)
print("Acceso a elemento anidado:", tupla_anidada[1][0])  # 3