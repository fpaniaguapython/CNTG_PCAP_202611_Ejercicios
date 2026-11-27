import sys

# Guardamos la entrada estándar original
entrada_original = sys.stdin

# Redirigimos stdin al fichero
fichero = open("datos_stdin.txt", "r")
sys.stdin = fichero

# Leemos los datos como si procedieran del teclado
nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
ciudad = input("Introduce tu ciudad: ")

print("Datos introducidos:")
print(nombre)
print(edad)
print(ciudad)

# Restauramos stdin y cerramos el fichero
sys.stdin = entrada_original
fichero.close()