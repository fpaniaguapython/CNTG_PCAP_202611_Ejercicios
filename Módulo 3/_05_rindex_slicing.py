nombre_fichero = input('Nombre de fichero:')

# Busco el punto empezando por la derecha
posicion_punto = nombre_fichero.rindex('.')

 # Desde la posición del punto hasta el final
extension = nombre_fichero[posicion_punto+1:]

print('Extensión:', extension)