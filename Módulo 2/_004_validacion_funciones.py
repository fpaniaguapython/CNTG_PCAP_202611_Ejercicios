def guardar_ficha(nombre: str, salario: int, retencion: float):
    '''
    Comprobar que los tipos son correctos.
    Comprobar que el nombre no está vacio: len(nombre.strip())>0
    Comprobar que el salario es positivo: salario>0
    '''

    # nombre.lower() --> Obtiene una versión en minúsculas del nombre
    # mode='wt' --> w(write), t(text)
    fichero = open(nombre.lower()+'.txt', mode='wt', encoding='utf-8')
    fichero.write(nombre) # Escribe en el fichero
    fichero.write('#')
    fichero.write(str(salario)) # La función str convierte a str el argumento
    fichero.write('#')
    fichero.write(str(retencion)) # La función str convierte a str el argumento 
    fichero.close()

guardar_ficha('Fernando', 15000, 15.3)