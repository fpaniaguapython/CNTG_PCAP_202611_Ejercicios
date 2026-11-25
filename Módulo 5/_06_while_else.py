import random

numero_secreto = random.randint(1,9)
# print(numero_secreto)
intentos = 0

while intentos < 3:
    numero_candidato = int(input('Número candidato:'))
    if numero_candidato==numero_secreto:
        print(f'Has descubierto el número: {numero_secreto}')
        break # Impide que se ejecute el else
    intentos+=1
else: # Se ejecuta si se ha recorrido todo el bucle
    print('Eres un fraude como adivino')


