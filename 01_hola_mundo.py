"""
Módulo de saludo básico
Demuestra funciones simples y type hints en Python
"""

def saludar(nombre: str) -> str:
    """Retorna un saludo personalizado"""
    return f"Hola, {nombre}!"

def despedir(nombre: str) -> str:
    """Retorna un mensaje de despedida"""
    return f"¡Adiós, {nombre}!"

if __name__ == "__main__":
    print(saludar("Daniel Diaz ñd"))
    print(despedir("Daniel Diaz ñd"))
