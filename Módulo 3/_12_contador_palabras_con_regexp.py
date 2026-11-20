import re

with open('el_quijote.txt', mode='r', encoding='utf-8') as fichero:
    texto = fichero.read()

lista_palabras = re.findall(r'\w+', texto)
lista_palabras = [palabra.lower() for palabra in lista_palabras]
conjunto_palabras = set(lista_palabras)

for palabra in conjunto_palabras:
    print(palabra)

print(f'He encontrado {len(lista_palabras)} palabras')
print(f'He encontrado {len(conjunto_palabras)} palabras distintas')