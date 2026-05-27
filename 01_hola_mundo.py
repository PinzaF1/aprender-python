"""
Módulo de saludo básico
Demuestra funciones simples y type hints en Python
Autor: Carlos Pinza
"""

def saludar(nombre: str) -> str:
    """Retorna un saludo personalizado al usuario"""
    return f"Hola, {nombre}!"

def despedir(nombre: str) -> str:
    """Retorna un mensaje de despedida personalizado"""
    return f"¡Adiós, {nombre}!"

if __name__ == "__main__":
    print(saludar("Daniel Diaz ñd"))
    print(despedir("Daniel Diaz ñd"))
