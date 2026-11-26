# - Tanto readline como readlines leen el salto de línea del final de la misma.
# - Conviene eliminar dicho salto de línea --> list comprenhension es un buena
# manera.

with open('_16_metodo_readlines.py', mode='rt', encoding='utf-8') as fichero:
    lineas = fichero.readlines()

# lineas_sin_salto_de_linea = [linea.strip() for linea in lineas] # Elimina sangrado y salto de línea
lineas_sin_salto_de_linea = [linea.rstrip() for linea in lineas] # Elimina sangrado y salto de línea
pass