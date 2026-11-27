import time

####################################
# - Con una función 'normal', hasta que no están todos los datos disponibles
# no se devuelven. 
# - Todos los datos se encuentran simultáneamente en memoria.
####################################

def cargar_datos_con_return():
    # Tarda 5 segundos en devolver TODOS los datos
    lista = []
    for x in range(0,10):
        lista.append(x)
        time.sleep(0.5)
    return lista

print('Cargando datos (con return)...')
datos = cargar_datos_con_return()
for dato in datos:
    print('Dato:', dato)

####################################
# - Con un generador los datos se van devolviendo según se dispone de ellos. 
# - En memoria solo hay un dato en un momento determinado.
####################################

def cargar_datos_con_generador():
    # Tarda 5 segundos en devolver TODOS los datos
    for x in range(0,10):
        yield x
        time.sleep(0.5)

print('Cargando datos (con generador -yield-)...')

for dato in cargar_datos_con_generador():
    print("Dato:", dato)