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

# 2. CONTEXT MANAGERS
# Los context managers permiten manejar recursos de forma segura

class MiContextManager:
    def __enter__(self):
        print("Entrando al contexto")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Saliendo del contexto")
        return False

# Usar context manager
# with MiContextManager() as cm:
#     print("Dentro del contexto")

# 3. METACLASES
# Las metaclases son clases cuyas instancias son clases

class MetaclaseMi(type):
    def __new__(mcs, nombre, bases, attrs):
        print(f"Creando clase: {nombre}")
        return super().__new__(mcs, nombre, bases, attrs)

class MiClase(metaclass=MetaclaseMi):
    def __init__(self, valor):
        self.valor = valor

# Crear instancia
# obj = MiClase(42)
# print(obj.valor)
