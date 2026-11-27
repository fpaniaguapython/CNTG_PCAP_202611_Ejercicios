import sqlite3

conexion = sqlite3.connect("peliculas.sqlite")
conexion.execute("PRAGMA journal_mode=WAL")

cursor = conexion.cursor()

# Iniciamos una transacción
cursor.execute("BEGIN")

# Borramos los registros 11 y 12 si existen
cursor.execute("""
DELETE FROM peliculas
WHERE id IN (11, 12)
""")

# Insertamos las películas
cursor.execute("""
INSERT INTO peliculas VALUES (11, 'Tiburón', 'Steven Spielberg', 1975)
""")

cursor.execute("""
INSERT INTO peliculas VALUES (12, 'Alien', 'Ridley Scott', 1979)
""")

# Confirmamos la transacción
conexion.commit()

conexion.close()