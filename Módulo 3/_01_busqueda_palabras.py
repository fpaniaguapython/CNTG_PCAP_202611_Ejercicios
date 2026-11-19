with open('el_quijote.txt', mode='r', encoding='utf-8') as fichero:
    texto = fichero.read()

#print(texto[:100])

# Solicitar una palabra al usuario y mostrar cuantas veces aparece en el texto.

palabra = input('Introduce una palabra:')

# numero_veces = texto.count(palabra) # Búsqueda diferenciando mayúsculas y minúsculas -> 88
# numero_veces = texto.upper().count(palabra.upper()) # 91
# numero_veces = texto.lower().count(palabra.lower()) # 91
numero_veces = texto.casefold().count(palabra.casefold()) # 91

print(f'La palabra {palabra} aparece {numero_veces} en El Quijote')

