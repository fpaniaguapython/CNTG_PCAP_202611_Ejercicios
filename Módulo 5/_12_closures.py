def enclosing_function(argumento):
    def inner_function():
        print('Soy una closure:',argumento)
    return inner_function

alimento = 'patata'
funcion_mostrar_patata = enclosing_function(alimento)
alimento = 'cebolla'
funcion_mostrar_cebolla = enclosing_function(alimento) 

funcion_mostrar_patata() # Soy una closure: patata
funcion_mostrar_cebolla() # Soy una closure: cebolla


