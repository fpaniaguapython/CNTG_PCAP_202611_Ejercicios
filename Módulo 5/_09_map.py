def get_text_factura(factura):
    return f'Escribiendo la factura... {factura}'

facturas = ('F1', 'F2', 'F3', 'F4')

# SIN MAP
print('***SIN MAP***')
for factura in facturas:
    print(get_text_factura(factura))

# CON MAP
print('***CON MAP***')
resultados = map(get_text_factura, facturas) # Devuelve un generador

for resultado in resultados:
    print(resultado)

# CON MAP Y LAMBDA
print('***CON MAP Y LAMBDA***')
resultados = map(lambda factura : f'Escribiendo la factura... {factura}', facturas)

for resultado in resultados:
    print(resultado)