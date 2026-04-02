# Diccionarios Avanzados en Python
# Explorando características y métodos avanzados de diccionarios

# 1. Crear diccionarios de diferentes formas
dict_literal = {'nombre': 'Juan', 'edad': 30}
dict_constructor = dict(nombre='María', edad': 25)
dict_comprehension = {x: x**2 for x in range(5)}

print("Diccionario literal:", dict_literal)
print("Diccionario con dict():", dict_constructor)
print("Diccionario con comprehension:", dict_comprehension)

# 2. Métodos útiles de diccionarios
persona = {'nombre': 'Carlos', 'edad': 35, 'ciudad': 'Madrid'}
print("\nMétodos de diccionarios:")
print("Keys:", persona.keys())
print("Values:", persona.values())
print("Items:", persona.items())

# 3. Usar get() para evitar errores
print("\nUsando get():")
print("Profesión:", persona.get('profesión', 'No especificada'))

# 4. Actualizar diccionarios
persona.update({'profesión': 'Ingeniero', 'edad': 36})
print("\nDiccionario actualizado:", persona)

# 5. Diccionarios anidados
estudiantes = {
    'est001': {'nombre': 'Ana', 'calificación': 9.5},
    'est002': {'nombre': 'Bruno', 'calificación': 8.7},
}
print("\nEstudiantes:", estudiantes)
