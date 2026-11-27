
# Este ejemplo muestra el uso de map sobre una select realizada sobre una
# base de datos, pero dicho uso no aporta ninguna ventaja frente a recorrer
# el cursor con un bucle for. 
# 
# El uso del for en lugar de map en este caso es más apropiado
# porque simplifica la legibilidad del código.

import sqlite3

# 0. Crear la función que devuelve información sobre la película
def obtener_info_pelicula(pelicula):
    return (pelicula["titulo"],pelicula["año"])

# 1. Conectar con la base de datos (se crea si no existe)
conexion = sqlite3.connect("peliculas.sqlite")
conexion.row_factory = sqlite3.Row # Permite acceder a las columnas por su nombre, no solo por su índice
conexion.execute("PRAGMA journal_mode=WAL")


# 2. Crear un cursor
cursor = conexion.cursor()

# 3. Crear la tabla peliculas
cursor.execute("""
CREATE TABLE IF NOT EXISTS peliculas (
    id INTEGER PRIMARY KEY,
    titulo TEXT,
    director TEXT,
    año INTEGER
)
""")

# 4. Insertar 10 películas
peliculas = [
    (1, "Titanic", "James Cameron", 1997),
    (2, "Gladiator", "Ridley Scott", 2000),
    (3, "Avatar", "James Cameron", 2009),
    (4, "Origen", "Christopher Nolan", 2010),
    (5, "Pulp Fiction", "Quentin Tarantino", 1994),
    (6, "Interstellar", "Christopher Nolan", 2014),
    (7, "Matrix", "Lana y Lilly Wachowski", 1999),
    (8, "El padrino", "Francis Ford Coppola", 1972),
    (9, "Forrest Gump", "Robert Zemeckis", 1994),
    (10, "Gladiator II", "Ridley Scott", 2024)
]

# Borramos los registros 11 y 12 si existen
cursor.execute("DELETE FROM peliculas")

cursor.executemany(
    "INSERT OR IGNORE INTO peliculas VALUES (?, ?, ?, ?)",
    peliculas
)

# 5. Guardar los cambios
conexion.commit()

# 6. Consultar todas las películas
cursor.execute("SELECT * FROM peliculas")

# 7. Mostrar los resultados

input('Pulsa ENTER para continuar')

# Con un for:
# for pelicula in cursor:
#     print(obtener_info_pelicula(pelicula=pelicula))

# Con un map
anyos = map(obtener_info_pelicula, cursor)
for anyo in anyos:
   print(anyo)


# 8. Cerrar la conexión
conexion.close()
