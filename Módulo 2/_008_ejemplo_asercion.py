def calcular_importe(importe_base: int, impuesto: float):
    # assert importe_base>0
    assert importe_base>0, 'El importe base debe ser positivo'
    importe_total = importe_base + importe_base * impuesto
    return importe_total

total = calcular_importe(-1000, 0.21)
print(total)
