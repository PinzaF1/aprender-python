# 11_excepciones.py - Aprendiendo excepciones en Python

# Las excepciones manejan errores durante la ejecución
def dividir(a, b):
    try:
        resultado = a / b
        print(f"El resultado de {a} / {b} es {resultado}")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")
    except TypeError:
        print("Error: Los valores deben ser números.")
    finally:
        print("Operación completada.")

# Ejemplos
dividir(10, 2)
dividir(10, 0)
dividir(10, "a")