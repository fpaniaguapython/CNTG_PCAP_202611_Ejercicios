def duplicar(numero_interno):
    numero_interno=numero_interno*2

numero = 10
duplicar(numero) # Pasa la lista por valor 
print(numero) # 10

def agregar_elemento(lista_interna):
    lista_interna.append(len(lista_interna))

lista = [1,4,8]
agregar_elemento(lista) # Pasa la lista por referencia
print(lista) # [1,4,8,3]