def comando_1():
    print("C1")

def comando_2():
    print("C2")

def comando_3():
    print("C3")

def ejecutador_funciones(funcion):
    funcion()

tupla_funciones = (comando_1, comando_2, comando_3)

for f in tupla_funciones:
    ejecutador_funciones(f)

