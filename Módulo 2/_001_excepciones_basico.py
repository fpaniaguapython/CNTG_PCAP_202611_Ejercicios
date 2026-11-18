lista_compra = ['Aceite', 'Leche', 'Pan', 'Galletas']

try:
    indice_producto = int(input('Introduce índice de producto:'))
    producto = lista_compra[indice_producto]
    print(f'El producto seleccionado es: {producto}')
except IndexError as ie:
    print(f'El producto {indice_producto} no existe en la cesta')
    #print(ie)
except ValueError as ve:
    print(f'Error. Debe introducir un número entero entre 0 y {len(lista_compra)-1}')
    #print(ve)