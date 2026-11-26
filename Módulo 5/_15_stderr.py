import sys
try:
    fichero_errores = open("salida_errores.txt", "w")
    fichero_salida_normal = open("salida_normal.txt", "w")

    sys.stderr = fichero_errores
    sys.stdout = fichero_salida_normal

    # print("Esto es un error", file=sys.stderr) # Escritura en la salida de error
    print('Esto es correcto')
    raise Exception('Esto es un error')
finally:
    fichero_errores.close()
    fichero_salida_normal.close()