# Ejercicio de conjuntos

# Crear un conjunto con palabras prohibidas
prohibiciones = {'maldición', 'insulto', 'grosería', 'ofensa'}

# Solicitar al usuario que introduzca una opinión
opinion = input('Introduce tu opinión: ')
palabras_opinion = opinion.lower().split()

# Comprobar si la palabra está en el conjunto de palabras prohibidas
palabras_prohibidas_utilizadas = prohibiciones.intersection(palabras_opinion)

 # Devuelve un conjunto con los elementos en común entre el conjunto de prohibiciones y la palabra introducida por el usuario
if len(palabras_prohibidas_utilizadas)>0:
    print('Ha utilizado una palabra prohibida:', palabras_prohibidas_utilizadas)
else:
    print('No ha utilizado una palabra prohibida')