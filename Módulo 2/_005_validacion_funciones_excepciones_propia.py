class NombreVacioError(Exception):
    pass

def guardar_ficha(nombre: str, salario: int, retencion: float):
    """
    Comprobar que los tipos son correctos.
    Comprobar que el nombre no está vacio: len(nombre.strip())>0
    Comprobar que el salario es positivo: salario>0
    """
    # Comprobar que los tipos son correctos.
    if (not isinstance(nombre, str)
        or not isinstance(salario, int) 
        or not isinstance(retencion, float)):
        raise TypeError('Los tipos de los argumentos son incorrectos')

    # Comprobar que el nombre no está vacio: len(nombre.strip())>0
    if (len(nombre.strip())==0):
        raise NombreVacioError('No se admiten nombres vacíos')

    # Comprobar que el salario es positivo: salario>0
    if salario<=0:
        raise ValueError('El salario debe ser positivo')

    # nombre.lower() --> Obtiene una versión en minúsculas del nombre
    # mode='wt' --> w(write), t(text)
    fichero = open(nombre.lower()+'.txt', mode='wt', encoding='utf-8')
    fichero.write(nombre) # Escribe en el fichero
    fichero.write('#')
    fichero.write(str(salario)) # La función str convierte a str el argumento
    fichero.write('#')
    fichero.write(str(retencion)) # La función str convierte a str el argumento 
    fichero.close()

try:
    guardar_ficha("", 2000, 15.0)
except NombreVacioError as nve:
    print('Excepción de nombre vacío:', nve)
except Exception as ex:
    print(ex)