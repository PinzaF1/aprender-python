"""
Juego de Minesweeper (Campo Minado)
Un clásico juego donde debes descubrir todas las casillas sin encontrar las minas.
"""

import random
from typing import List, Tuple

class Minesweeper:
    def __init__(self, filas: int = 8, columnas: int = 8, minas: int = 10):
        """
        Inicializa el juego de Minesweeper.
        
        Args:
            filas: Número de filas del tablero
            columnas: Número de columnas del tablero
            minas: Número de minas a colocar
        """
        self.filas = filas
        self.columnas = columnas
        self.minas = minas
        self.tablero = [[0 for _ in range(columnas)] for _ in range(filas)]
        self.revelado = [[False for _ in range(columnas)] for _ in range(filas)]
        self.marcado = [[False for _ in range(columnas)] for _ in range(filas)]
        self.juego_activo = True
        self.ganado = False
        
        self._colocar_minas()
        self._calcular_numeros()
    
    def _colocar_minas(self) -> None:
        """Coloca las minas aleatoriamente en el tablero."""
        minadas = 0
        while minadas < self.minas:
            fila = random.randint(0, self.filas - 1)
            col = random.randint(0, self.columnas - 1)
            
            if self.tablero[fila][col] != -1:  # -1 representa una mina
                self.tablero[fila][col] = -1
                minadas += 1
    
    def _calcular_numeros(self) -> None:
        """Calcula el número de minas adyacentes para cada casilla."""
        for fila in range(self.filas):
            for col in range(self.columnas):
                if self.tablero[fila][col] != -1:
                    self.tablero[fila][col] = self._contar_minas_adyacentes(fila, col)
    
    def _contar_minas_adyacentes(self, fila: int, col: int) -> int:
        """Cuenta las minas alrededor de una casilla."""
        contador = 0
        for df in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if df == 0 and dc == 0:
                    continue
                nf, nc = fila + df, col + dc
                if 0 <= nf < self.filas and 0 <= nc < self.columnas:
                    if self.tablero[nf][nc] == -1:
                        contador += 1
        return contador
    
    def revelar(self, fila: int, col: int) -> bool:
        """
        Revela una casilla. Retorna False si hay mina.
        
        Args:
            fila: Fila de la casilla
            col: Columna de la casilla
            
        Returns:
            True si es seguro, False si hay mina
        """
        if not (0 <= fila < self.filas and 0 <= col < self.columnas):
            print("❌ Coordenadas fuera del tablero")
            return True
        
        if self.revelado[fila][col]:
            print("⚠️  Esta casilla ya fue revelada")
            return True
        
        if self.marcado[fila][col]:
            print("⚠️  Esta casilla está marcada como mina")
            return True
        
        self.revelado[fila][col] = True
        
        # Si es una mina, se acabó el juego
        if self.tablero[fila][col] == -1:
            self.juego_activo = False
            return False
        
        # Si es 0, revelar casillas adyacentes automáticamente
        if self.tablero[fila][col] == 0:
            for df in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if df == 0 and dc == 0:
                        continue
                    nf, nc = fila + df, col + dc
                    if (0 <= nf < self.filas and 0 <= nc < self.columnas and 
                        not self.revelado[nf][nc] and not self.marcado[nf][nc]):
                        self.revelar(nf, nc)
        
        return True
    
    def marcar(self, fila: int, col: int) -> None:
        """Marca o desmarca una casilla como mina."""
        if not (0 <= fila < self.filas and 0 <= col < self.columnas):
            print("❌ Coordenadas fuera del tablero")
            return
        
        if self.revelado[fila][col]:
            print("⚠️  No puedes marcar una casilla revelada")
            return
        
        self.marcado[fila][col] = not self.marcado[fila][col]
        accion = "marcada" if self.marcado[fila][col] else "desmarcada"
        print(f"✓ Casilla {accion} como mina")
    
    def verificar_victoria(self) -> bool:
        """Verifica si el jugador ha ganado."""
        for fila in range(self.filas):
            for col in range(self.columnas):
                # Si una casilla sin mina no está revelada, no ganó
                if self.tablero[fila][col] != -1 and not self.revelado[fila][col]:
                    return False
        return True
    
    def mostrar_tablero(self, mostrar_minas: bool = False) -> None:
        """
        Muestra el tablero actual.
        
        Args:
            mostrar_minas: Si True, muestra todas las minas (cuando pierdes)
        """
        print("\n  ", end="")
        for col in range(self.columnas):
            print(f"{col:2}", end=" ")
        print("\n" + "  " + "-" * (self.columnas * 3))
        
        for fila in range(self.filas):
            print(f"{fila}| ", end="")
            for col in range(self.columnas):
                if mostrar_minas and self.tablero[fila][col] == -1:
                    print(" 💣", end=" ")
                elif self.revelado[fila][col]:
                    if self.tablero[fila][col] == -1:
                        print(" 💣", end=" ")
                    elif self.tablero[fila][col] == 0:
                        print("  ·", end=" ")
                    else:
                        print(f"  {self.tablero[fila][col]}", end=" ")
                elif self.marcado[fila][col]:
                    print("  🚩", end=" ")
                else:
                    print("  ■", end=" ")
            print()
        print()
    
    def mostrar_estadisticas(self) -> None:
        """Muestra las estadísticas del juego."""
        reveladas = sum(sum(1 for x in fila if x) for fila in self.revelado)
        marcadas = sum(sum(1 for x in fila if x) for fila in self.marcado)
        total = self.filas * self.columnas
        
        print(f"\n📊 ESTADÍSTICAS:")
        print(f"  Casillas reveladas: {reveladas}/{total}")
        print(f"  Casillas marcadas: {marcadas}/{self.minas}")
        print(f"  Minas totales: {self.minas}\n")


def jugar():
    """Función principal para jugar al Minesweeper."""
    print("=" * 50)
    print("🎮 BIENVENIDO AL MINESWEEPER (CAMPO MINADO)")
    print("=" * 50)
    print("\n📋 INSTRUCCIONES:")
    print("  • Ingresa: fila columna (para revelar)")
    print("  • Ingresa: m fila columna (para marcar/desmarcar)")
    print("  • Ingresa: q (para salir)")
    print("  • Evita las 💣 minas")
    print("  • Revela todas las casillas seguras para ganar")
    
    # Opciones de dificultad
    print("\n⚙️  SELECCIONA DIFICULTAD:")
    print("  1. Fácil (8x8, 10 minas)")
    print("  2. Normal (10x10, 20 minas)")
    print("  3. Difícil (12x12, 40 minas)")
    
    while True:
        try:
            opcion = input("\nOpción (1-3): ").strip()
            if opcion == "1":
                juego = Minesweeper(8, 8, 10)
                break
            elif opcion == "2":
                juego = Minesweeper(10, 10, 20)
                break
            elif opcion == "3":
                juego = Minesweeper(12, 12, 40)
                break
            else:
                print("❌ Opción inválida")
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            return
    
    # Bucle principal del juego
    while juego.juego_activo:
        juego.mostrar_tablero()
        juego.mostrar_estadisticas()
        
        try:
            entrada = input("👉 Tu movimiento: ").strip().lower()
            
            if entrada == "q":
                print("👋 ¡Gracias por jugar!")
                break
            
            partes = entrada.split()
            
            if partes[0] == "m" and len(partes) == 3:
                # Marcar casilla
                fila, col = int(partes[1]), int(partes[2])
                juego.marcar(fila, col)
            elif len(partes) == 2:
                # Revelar casilla
                fila, col = int(partes[0]), int(partes[1])
                if not juego.revelar(fila, col):
                    print("\n💥 ¡EXPLOTASTE! ¡Pisaste una mina!")
                    juego.mostrar_tablero(mostrar_minas=True)
                    print("😢 GAME OVER")
                    break
                elif juego.verificar_victoria():
                    juego.mostrar_tablero()
                    print("🎉 ¡¡¡GANASTE!!! ¡Completaste el nivel sin pisar minas!")
                    juego.ganado = True
                    break
            else:
                print("❌ Entrada inválida. Usa 'fila columna' o 'm fila columna'")
        
        except ValueError:
            print("❌ Las coordenadas deben ser números")
        except KeyboardInterrupt:
            print("\n\n👋 ¡Hasta luego!")
            break
    
    # Resumen final
    print("\n" + "=" * 50)
    if juego.ganado:
        print("🏆 ¡FELICIDADES! ¡GANASTE EL JUEGO!")
    print("=" * 50)


if __name__ == "__main__":
    jugar()
