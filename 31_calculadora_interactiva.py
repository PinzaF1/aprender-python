#!/usr/bin/env python3
"""
Calculadora Interactiva
Una aplicación de calculadora que permite realizar operaciones matemáticas básicas.
"""

def mostrar_menu():
    """Muestra el menú principal de la calculadora."""
    print("\n" + "="*50)
    print("CALCULADORA INTERACTIVA")
    print("="*50)
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz Cuadrada")
    print("7. Módulo (Residuo)")
    print("8. Salir")
    print("="*50)

def obtener_numeros():
    """Obtiene dos números del usuario."""
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        return num1, num2
    except ValueError:
        print("❌ Error: Ingrese números válidos")
        return None, None

def suma(a, b):
    """Realiza una suma."""
    return a + b

def resta(a, b):
    """Realiza una resta."""
    return a - b

def multiplicacion(a, b):
    """Realiza una multiplicación."""
    return a * b

def division(a, b):
    """Realiza una división."""
    if b == 0:
        return "❌ Error: No se puede dividir entre cero"
    return a / b

def potencia(a, b):
    """Calcula la potencia."""
    return a ** b

def raiz_cuadrada(a, b=None):
    """Calcula la raíz cuadrada."""
    if a < 0:
        return "❌ Error: No se puede calcular raíz de número negativo"
    return a ** 0.5

def modulo(a, b):
    """Calcula el módulo (residuo de la división)."""
    if b == 0:
        return "❌ Error: No se puede calcular módulo entre cero"
    return a % b

def main():
    """Función principal de la calculadora."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una operación (1-8): ").strip()
        
        if opcion == '8':
            print("\n¡Gracias por usar la calculadora! 👋")
            break
        
        if opcion in ['1', '2', '3', '4', '5', '7']:
            num1, num2 = obtener_numeros()
            if num1 is None:
                continue
        elif opcion == '6':
            try:
                num1 = float(input("Ingrese el número: "))
            except ValueError:
                print("❌ Error: Ingrese un número válido")
                continue
        else:
            print("❌ Opción inválida. Por favor, seleccione una opción válida (1-8)")
            continue
        
        # Realizar la operación
        if opcion == '1':
            resultado = suma(num1, num2)
            print(f"\n✅ {num1} + {num2} = {resultado}")
        elif opcion == '2':
            resultado = resta(num1, num2)
            print(f"\n✅ {num1} - {num2} = {resultado}")
        elif opcion == '3':
            resultado = multiplicacion(num1, num2)
            print(f"\n✅ {num1} × {num2} = {resultado}")
        elif opcion == '4':
            resultado = division(num1, num2)
            print(f"\n✅ {num1} ÷ {num2} = {resultado}")
        elif opcion == '5':
            resultado = potencia(num1, num2)
            print(f"\n✅ {num1} ^ {num2} = {resultado}")
        elif opcion == '6':
            resultado = raiz_cuadrada(num1)
            print(f"\n✅ √{num1} = {resultado}")
        elif opcion == '7':
            resultado = modulo(num1, num2)
            print(f"\n✅ {num1} % {num2} = {resultado}")

if __name__ == "__main__":
    main()
