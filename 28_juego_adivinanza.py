"""
Juego de Adivinanza del Número
El usuario debe adivinar un número aleatorio entre 1 y 100
"""

import random


def juego_adivinanza():
    """
    Juego interactivo donde el usuario adivina un número aleatorio.
    """
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False
    
    print("=" * 50)
    print("¡Bienvenido al Juego de Adivinanza del Número!")
    print("=" * 50)
    print("\nDebes adivinar un número entre 1 y 100")
    print("¡A ver si tienes suerte!\n")
    
    while not adivinado:
        try:
            # Obtener entrada del usuario
            entrada = input("¿Cuál es tu adivinanza? ")
            numero_usuario = int(entrada)
            
            # Validar que esté en el rango
            if numero_usuario < 1 or numero_usuario > 100:
                print("❌ Por favor, ingresa un número entre 1 y 100\n")
                continue
            
            intentos += 1
            
            # Comparar el número
            if numero_usuario == numero_secreto:
                adivinado = True
                print(f"\n🎉 ¡GANASTE! ¡Adivinaste el número {numero_secreto}!")
                print(f"📊 Lo lograste en {intentos} intentos")
                
                # Mostrar estadísticas
                if intentos <= 5:
                    print("⭐ ¡Excelente! Eres un profesional")
                elif intentos <= 10:
                    print("👍 ¡Muy bien! Buen trabajo")
                else:
                    print("💪 ¡No te rindas! Sigue practicando")
            
            elif numero_usuario < numero_secreto:
                diferencia = numero_secreto - numero_usuario
                if diferencia > 20:
                    pista = "mucho más alto"
                elif diferencia > 10:
                    pista = "bastante más alto"
                else:
                    pista = "un poco más alto"
                print(f"❄️  El número secreto es {pista}")
                print(f"📍 Intentos: {intentos}\n")
            
            else:  # numero_usuario > numero_secreto
                diferencia = numero_usuario - numero_secreto
                if diferencia > 20:
                    pista = "mucho más bajo"
                elif diferencia > 10:
                    pista = "bastante más bajo"
                else:
                    pista = "un poco más bajo"
                print(f"🔥 El número secreto es {pista}")
                print(f"📍 Intentos: {intentos}\n")
        
        except ValueError:
            print("❌ Por favor, ingresa un número válido\n")


def menu_principal():
    """
    Menú principal del juego.
    """
    mientras = True
    
    while mientras:
        print("\n" + "=" * 50)
        print("MENÚ PRINCIPAL")
        print("=" * 50)
        print("1. Jugar")
        print("2. Instrucciones")
        print("3. Salir")
        print("=" * 50)
        
        opcion = input("Selecciona una opción (1-3): ").strip()
        
        if opcion == "1":
            juego_adivinanza()
        
        elif opcion == "2":
            print("\n" + "=" * 50)
            print("INSTRUCCIONES")
            print("=" * 50)
            print("""
1. La computadora elige un número secreto entre 1 y 100
2. Tú debes adivinarlo
3. Por cada intento, la computadora te da pistas:
   - Dice si el número secreto es más alto o más bajo
   - Mientras más cerca estés, la pista es más precisa
4. ¡Intenta adivinarlo en el menor número de intentos!
            """)
        
        elif opcion == "3":
            print("\n👋 ¡Gracias por jugar! ¡Hasta luego!")
            mientras = False
        
        else:
            print("❌ Opción no válida. Por favor intenta de nuevo.")


if __name__ == "__main__":
    menu_principal()
