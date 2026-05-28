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

def saludar_formal(nombre: str) -> str:
    """Retorna un saludo formal con título"""
    return f"Estimado/a {nombre}, es un placer saludarle."

if __name__ == "__main__":
    print(saludar("Daniel Diaz ñd"))
    print(despedir("Daniel Diaz ñd"))
    print(saludar_formal("Daniel Diaz ñd"))
