import random

lista = [1,2,4,-1,8,15]

# Estrella

lista_ordenada = sorted(lista) # Función. Generar un copia de la lista ordenada de menor a mayor.

lista.sort() # Método. Ordenar la lista de menor a mayor 

print(lista_ordenada)
print(lista)

lista_ordenada = sorted(lista, reverse=True) # Función. Generar un copia de la lista ordenada de mayor a menor.

lista.sort(reverse=True) # Ordena la lista de mayor a menor.

print(lista_ordenada)
print(lista)

# ('Modelo', potencia, precio)
coches = [('Seat Panda',100,3000), ('Ford Focus',800,40000), ('Ferrari F40',500,6000)]
coches.sort() # Ordena por el nombre del coche.

coches.sort(key=lambda coche : coche[1], reverse=True) # Ordenación por potencia de mayor a menor
print(coches) # [('Ford Focus', 800, 40000), ('Ferrari F40', 500, 6000), ('Seat Panda', 100, 3000)]

coches.sort(key=lambda coche : coche[2]) # Ordenación de menor a mayor por precio
print(coches) # [('Seat Panda', 100, 3000), ('Ferrari F40', 500, 6000), ('Ford Focus', 800, 40000)]

# Ordenación por potencia de menor a mayor SIN UTILIZAR lambda
def obtener_potencia(coche):
    return coche[1]

coches.sort(key=obtener_potencia) # [('Seat Panda', 100, 3000), ('Ferrari F40', 500, 6000), ('Ford Focus', 800, 40000)]
print(coches)

# Utilizando closures

def generar_funcion_cuantificacion(indice):
    def cuantificador(coche):
        return coche[indice]
    return cuantificador

cuantificador_potencia = generar_funcion_cuantificacion(1)
cuantificador_precio = generar_funcion_cuantificacion(2)

coches.sort(key=cuantificador_potencia, reverse=True)
print(coches) # [('Ford Focus', 800, 40000), ('Ferrari F40', 500, 6000), ('Seat Panda', 100, 3000)]