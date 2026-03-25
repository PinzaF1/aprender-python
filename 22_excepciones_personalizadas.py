# 22_excepciones_personalizadas.py
# Ejemplo de excepción personalizada y manejo.

class SaldoInsuficienteError(Exception):
    """Excepción para saldo en cuenta insuficiente."""
    pass


def retirar(saldo, monto):
    if monto > saldo:
        raise SaldoInsuficienteError(f'Saldo insuficiente: saldo={saldo}, monto={monto}')
    return saldo - monto


def main():
    saldo = 100
    try:
        saldo = retirar(saldo, 150)
        print(f'Nouveau saldo: {saldo}')
    except SaldoInsuficienteError as ex:
        print('Error:', ex)

if __name__ == '__main__':
    main()
