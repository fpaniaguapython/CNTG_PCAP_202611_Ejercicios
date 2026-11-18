nombre_fichero = input('Introduce el nombre de un fichero:')

#rt -> r(read); t(text). Otros valores: w(write); b(binary)
fichero = None
try:
    fichero = open(file=nombre_fichero, mode='rt', encoding='utf-8')
    texto = fichero.read()
    print(texto) 
except FileNotFoundError as fnfe:
    print(f'No existe el fichero {nombre_fichero}')
except UnicodeDecodeError as ude:
    print(f'El fichero {nombre_fichero} no es un fichero de texto')
except PermissionError as pe:
    print('No tienes permisos para acceder al fichero.')
except Exception as ex:
    print('Ha ocurrido un error no controlado:', ex)
finally:
    if fichero is not None:
        fichero.close()
    