# 24_archivos_extras.py
# Ejemplo de lectura y escritura de archivos.

filename = 'archivo_ejemplo.txt'

with open(filename, 'w', encoding='utf-8') as f:
    f.write('Línea 1\n')
    f.write('Línea 2\n')

with open(filename, 'r', encoding='utf-8') as f:
    contenido = f.read()

if __name__ == '__main__':
    print('Contenido escrito y leído:')
    print(contenido)
