# ====================================
# Módulo 33: Conceptos Avanzados de Python
# ====================================

# 1. DECORADORES
# Los decoradores son funciones que modifican el comportamiento de otras funciones

def mi_decorador(func):
    """Un decorador simple que imprime antes y después de ejecutar una función"""
    def envoltura(*args, **kwargs):
        print(f"Ejecutando: {func.__name__}")
        resultado = func(*args, **kwargs)
        print(f"Finalizado: {func.__name__}")
        return resultado
    return envoltura

@mi_decorador
def saludar(nombre):
    return f"Hola, {nombre}!"

# Usar el decorador
# print(saludar("Carlos"))
