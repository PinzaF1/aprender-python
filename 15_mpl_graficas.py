"""Lección 15: Gráficas simples con matplotlib

Este ejemplo muestra cómo crear una gráfica interactiva en una ventana usando matplotlib.

Instalar dependencia (si no está instalada):
    python -m pip install matplotlib

Para ejecutar:
    python 15_mpl_graficas.py
"""

import math

import matplotlib.pyplot as plt


def main():
    # Crear datos de ejemplo: una curva seno
    x = [i * 0.1 for i in range(0, 63)]  # 0..6.2
    y = [math.sin(val) for val in x]

    plt.figure(figsize=(8, 4))
    plt.plot(x, y, marker="o", linestyle="-", color="#1f77b4")
    plt.title("Ejemplo de gráfica: seno")
    plt.xlabel("x")
    plt.ylabel("sin(x)")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
