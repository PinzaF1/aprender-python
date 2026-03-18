# 10_clases.py - Aprendiendo clases en Python

# Las clases son plantillas para crear objetos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

    def cumplir_anios(self):
        self.edad += 1
        print(f"¡Feliz cumpleaños! Ahora tengo {self.edad} años.")

# Crear una instancia de la clase
persona1 = Persona("Ana", 30)
print(persona1.saludar())

# Usar un método
persona1.cumplir_anios()


# Otra clase para practicar la creación de objetos
class Estudiante:
    def __init__(self, nombre, curso):
        self.nombre = nombre
        self.curso = curso

    def presentarse(self):
        return f"Hola, soy {self.nombre} y estudio {self.curso}."


# Crear y usar una instancia de Estudiante
estudiante1 = Estudiante("Luis", "Matemáticas")
print(estudiante1.presentarse())