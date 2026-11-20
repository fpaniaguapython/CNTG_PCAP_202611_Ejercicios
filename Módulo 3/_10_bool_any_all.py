# Todas devuelven valor booleano (True o False)

lista_vacia = []
parametros = ['3', '1a', 'a']
parametros_digitos = ['3', '4322', '8383']

# Función bool. Comprueba si la lista (o tupla) tiene contenido
tiene_contenido = bool(parametros)
print(tiene_contenido) # True
tiene_contenido = bool(lista_vacia)
print(tiene_contenido) # False

# Función any
tiene_algun_digito = any(parametro.isdigit() for parametro in parametros)
print(tiene_algun_digito) # True (por el 3)

# Función all
tiene_todos_digitos = all(parametro.isdigit() for parametro in parametros)
print(tiene_todos_digitos) # False

tiene_todos_digitos = all(parametro.isdigit() for parametro in parametros_digitos)
print(tiene_todos_digitos) # True