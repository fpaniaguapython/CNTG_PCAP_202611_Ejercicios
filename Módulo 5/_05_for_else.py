candidatos = [('Pedro',False), ('Ada',True), 
              ('Alberto',False), ('Irene',True), ('Santiago',False)]

for candidato in candidatos:
    if candidato[1]==True:
        print(f'El/la candidato/a {candidato[0]} es APTO/A')
        break # Impide que se ejecute el else
else: # Se ejecuta si se ha recorrido todo el bucle
    print('Hemos recorrido todo el bucle')