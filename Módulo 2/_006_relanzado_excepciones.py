def calcular_impuesto(importe: int, impuesto: float) -> float:
    if importe<=0:
        raise ValueError('El importe debe ser positivo')
    resultado = importe * impuesto
    return resultado 

def calcular_importe_total(importe: int, impuesto: float):
    try:
        importe_total = importe + calcular_impuesto(importe, impuesto)
        return importe_total
    except ValueError as ve:
        print('(calcular_importe_total) Ha ocurrido un error:', ve)
        # raise # Bare Raise (propagar la excepción sin argumentos).
        raise ve # Re-raising (propagar la excepción con argumentos).

if __name__=='__main__':
    try:
        resultado = calcular_importe_total(-1000, 0.21)
        print(resultado)
    except ValueError as ve:
        print('(__main__) Ha ocurrido un error:', ve)