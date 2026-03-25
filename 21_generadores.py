# 21_generadores.py
# Ejemplo de generador en Python

def contador(maximo):
    """Generador que cuenta de 1 a maximo."""
    n = 1
    while n <= maximo:
        yield n
        n += 1


def main():
    print('Contador usando generador:')
    for valor in contador(5):
        print(valor)

if __name__ == '__main__':
    main()
