class Factura:
    pass

def imprimir_factura(factura: Factura, copias: int) -> None:
    if not isinstance(factura, Factura):
        raise TypeError('Debes proporcionar una factura')
    if not isinstance(copias, int):
        raise TypeError('Debes proporcionar un número entero de copias')
    print('Imprimiendo factura...')
    pass
