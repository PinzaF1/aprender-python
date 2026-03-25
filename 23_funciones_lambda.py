# 23_funciones_lambda.py
# Ejemplo de funciones lambda y map/filter.

valores = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x * x, valores))
pares = list(filter(lambda x: x % 2 == 0, valores))

if __name__ == '__main__':
    print('Valores:', valores)
    print('Cuadrados:', cuadrados)
    print('Pares:', pares)
