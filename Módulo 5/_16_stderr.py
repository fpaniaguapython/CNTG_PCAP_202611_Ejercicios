import sys
import traceback # Contiene funciones para obtener, mostrar, formatear y manipular las trazas de las excepciones (tracebacks)

errores_original = sys.stderr

fichero_errores = open("salida_errores.txt", "w")
sys.stderr = fichero_errores

try:
    x = 10 / 0
except Exception:
    traceback.print_exc() # muestra la traza completa (traceback) de la última excepción producida
finally:
    sys.stderr = errores_original
    fichero_errores.close()