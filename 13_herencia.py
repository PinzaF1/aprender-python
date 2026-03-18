# 13_herencia.py - Ejemplo de herencia en Python

# La herencia permite crear clases que reutilizan y extienden el comportamiento de otra clase.
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        return f"{self.nombre} hace un sonido."


class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Guau!"


class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice: ¡Miau!"


# Uso de las clases
perro = Perro("Rex")
gato = Gato("Luna")

print(perro.hablar())
print(gato.hablar())
