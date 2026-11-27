import sys

# Guardamos la salida estándar original
salida_original = sys.stdout

try:
    # Abrimos el fichero y redirigimos stdout
    with open("salida_normal.txt", "w", encoding="utf-8") as fichero:
        sys.stdout = fichero

        print("Este texto se redirige al fichero 'salida_normal.txt'")
finally:
    # Restauramos stdout
    sys.stdout = salida_original