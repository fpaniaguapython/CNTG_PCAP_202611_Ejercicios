x = 5
y = 8

def sumar(x, y):
    # Dentro la función, en caso de que haya coincidencias entre
    # los nombres de variables locales (de la función) y globales
    # se toman las variables locales (las del ámbito más específico)
    resultado = x + y
    return resultado

resultado = sumar(x,y)
print(resultado)


