def sumar(numero_1, numero_2):
    return numero_1, numero_2

# Esta función sumar SUSTITUYE a la anterior
def sumar(numero_1=1, numero_2=12, numero_3=20):
    return numero_1+numero_2+numero_3

print(sumar())
print(sumar(8))
print(sumar(8,3))
print(sumar(numero_1=1, numero_3=15))

def add(numero_1: int, numero_2:int):
    return numero_1+numero_2

print(add(51,3))
print(add('Patata', 'Cebolla'))
print(add([1,2,3], [4,5,6]))
#print(add("Hola",8)) # Error