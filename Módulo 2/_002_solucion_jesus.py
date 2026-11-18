try:
    # Solicitamos el nombre del fichero
    nombre_fichero = input('Introduce el nombre de un fichero: ')
    # Abrimos el fichero en modo lectura de texto
    fichero = open(file=nombre_fichero, mode='rt', encoding='utf-8')
    # Leemos todo el contenido
    texto = fichero.read()
    # Mostramos el contenido
    print(texto)
    # Cerramos el fichero
    fichero.close()
except FileNotFoundError:
    # El fichero no existe o la ruta es incorrecta
    print('Error: El fichero no existe o la ruta es incorrecta.')
except PermissionError:
    # No tenemos permisos para acceder al fichero
    print('Error: No tienes permisos para acceder al fichero.')
except Exception as error:
    # Capturamos cualquier otro error
    print(f'Error inesperado: {error}')
else: # Se ejecuta cuando el bloque try no genere errores
    print('Fichero leído correctamente.')
finally:
    print('Ha terminado el proceso')