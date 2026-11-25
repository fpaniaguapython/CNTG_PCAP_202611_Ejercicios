numeros = [3, 8, 15, 8, 1]

# List comprenhension
dobles = [numero*2 for numero in numeros] # dobles es una lista
print(dobles) # [6, 16, 30, 16, 2]

# Set comprenhension
dobles = {numero*2 for numero in numeros} # dobles es un conjunto
print(dobles) # {16, 2, 6, 30}

# Dictionary comprenhension
dobles = {indice:numero*2 for indice, numero in enumerate(numeros)} # dobles es un diccionario
print(dobles) # {0: 6, 1: 16, 2: 30, 3: 16, 4: 2}

# Expresión generadora
# NOTA: Los paréntesis de la siguiente expresión no implican la construcción de
# una tupla, sino de un generador.
dobles = (numero*2 for numero in numeros) # dobles es un generador
print(type(dobles)) # <class 'generator'>
print(dobles) # <generator object <genexpr> at 0x000001D9BD64C580>
# Primer recorrido del generador
print('Primer recorrido del generador')
for doble in dobles:
    print(doble, end=',') # 6,16,30,16,2,
# Segundo recorrido del generador
print('\nSegundo recorrido del generador')
for dobles in dobles:
    print(doble, end=',') # No muestra nada. Los generadores se consumen.


# Obtener una tupla a partir una list comprenhension
numeros = [3, 8, 15, 8, 1]
tupla = tuple([numero*2 for numero in numeros])
print(type(tupla)) # <class 'tuple'>
print(tupla) # (6, 16, 30, 16, 2)