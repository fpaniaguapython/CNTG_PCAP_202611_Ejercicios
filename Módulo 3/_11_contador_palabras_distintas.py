with open('el_quijote.txt', mode='r', encoding='utf-8') as fichero:
    texto = fichero.read()

# Convertir el texto a minúsculas
# Método lower()
texto_minusculas = texto.lower()

# Reemplazar los caracteres . , -, ¿, ?, ¡, ! por un espacio en blanco
# Método replace
texto_limpio = texto_minusculas.replace('.', ' ').replace(',',' ').replace('-',' ').replace('¿',' ').replace('?',' ').replace('¡',' ').replace('!',' ')

# Obtener las palabras
# Método split
lista_palabras = texto_limpio.split()
print(f'He encontrado {len(lista_palabras)} palabras')

# Creación de un conjunto
# Función set
# Ejemplo:
#   lista = ['hola', 'libro', 'bombilla', 'libro', 'hoja'
#   conjunto = set(lista)
conjunto_palabras = set(lista_palabras)

# Contar el número de plabras que tiene el conjunto
# Función len
# Ejemplo:
#   len(conjunto)
print(f'He encontrado {len(conjunto_palabras)} palabras distintas')