# pip install levenshtein
import Levenshtein
import math

diccionario = ['patata', 'acelga', 'apio', 'puerro', 'Levenshtein']

palabra_buscada = input('Palabra:')

palabra_candidata = ''
distancia_minima = math.inf

# if palabra_buscada.upper() in [palabra.upper() for palabra in diccionario]:
if palabra_buscada in diccionario: # Distingue mayúsculas de minúsculas
    print(f'Tu palabras es {palabra_buscada}')
else:
    for palabra in diccionario:
        distancia = Levenshtein.distance(palabra_buscada, palabra)
        if distancia<distancia_minima:
            palabra_candidata = palabra
            distancia_minima = distancia
    print(f'A lo mejor querías decir {palabra_candidata}')
    print(f'Distancia:{distancia_minima}')

