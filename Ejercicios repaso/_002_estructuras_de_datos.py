# LISTAS
# Datos heterogéneos, mutables y ordenados
dias_semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 
               'sábado', 7]
print(dias_semana[1]) # Acceso al segundo elemento de la lista ('martes')
dias_semana[6]='domingo' # Modificación del último elemento de la lista
print(dias_semana) # Muestra la lista modificada

# TUPLAS
# Datos heterogéneos, inmutables y ordenados
dias_semana_tupla = ('lunes', 'martes', 'miércoles', 'jueves', 'viernes', 
                     'sábado', 7)
print(dias_semana_tupla[1]) # Acceso al segundo elemento de la tupla ('martes')

# CONJUNTOS
# Datos heterogéneos, mutables, desordenados y no permiten duplicados
ingredientes = {'harina', 'huevo', 'leche', 'azúcar', 'mantequilla', 'huevo'}
print(ingredientes)
# print(ingredientes[1]) # No se puede acceder por índice, ya que los conjuntos son desordenados
ingredientes.add('chocolate') # Agrega un nuevo elemento al conjunto

# DICCIONARIOS
# Datos heterogéneos, mutables, desordenados y permiten duplicados (no en claves)
medicamentos = {'paracetamol': 500, 'ibuprofeno': 400, 'amoxicilina': 250}
print(medicamentos['ibuprofeno']) # Acceso al valor asociado a la clave 'ibuprofeno'
medicamentos['amoxicilina'] = 500 # Modificación del valor asociado a la clave 'amoxicilina'
print(medicamentos) # Muestra el diccionario modificado