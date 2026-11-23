import re
import datetime

inicio = datetime.datetime.now().microsecond

with open('el_quijote.txt', mode='r', encoding='utf-8') as fichero:
    texto = fichero.read()

texto_minusculas = texto.lower()
#lista_palabras = re.findall(r'[a-zA-ZáéíóúÁÉÍÓÚüÜñÑ]+', texto)
lista_palabras = re.findall(r'[a-záéíóúüñ]+', texto_minusculas)
lista_palabras = [palabra.lower() for palabra in lista_palabras]
conjunto_palabras = set(lista_palabras)



print(f'He encontrado {len(lista_palabras)} palabras')
print(f'He encontrado {len(conjunto_palabras)} palabras distintas')

fin = datetime.datetime.now().microsecond

print(f'Total: {fin-inicio}microsegundos. Inicio: {inicio}. Fin: {fin}')