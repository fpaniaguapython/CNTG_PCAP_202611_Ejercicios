# Conjunto de ingredientes
ingredientes = {'harina', 'huevo', 'leche', 'azúcar', 'mantequilla', 'huevo'}
# Tupla de alergias
alergias = ('gluten', 'lactosa', 'frutos secos', 'huevo')

hay_peligro = ingredientes.isdisjoint(alergias) # Devuelve True si no hay elementos en común entre el conjunto y la tupla, False en caso contrario
if (hay_peligro):
    print("No hay peligro de alergias")
else:
    print("¡Cuidado! Hay ingredientes que pueden causar alergias")

ingredientes_peligro = ingredientes.intersection(alergias)
print("Ingredientes que pueden causar alergias:", ingredientes_peligro)