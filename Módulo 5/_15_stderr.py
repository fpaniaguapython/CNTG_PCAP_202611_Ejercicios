import sys

with open("salida_errores.txt", mode="w") as fichero_errores:
    sys.stderr = fichero_errores
    print("Ejecución con error", file=sys.stderr)
    
with open("salida_normal.txt", "w") as fichero_salida_normal:
    sys.stdout = fichero_salida_normal
    print("Ejecución correcta")