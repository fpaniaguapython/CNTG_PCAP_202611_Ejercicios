cadena = 'Me gusta Python'
cadena_ordenada = sorted(cadena) # Devuelve una lista con los caracteres ordenados de menor a mayor (punto de código)
print(cadena_ordenada) # [' ', ' ', 'M', 'P', 'a', 'e', 'g', 'h', 'n', 'o', 's', 't', 't', 'u', 'y']

cadena_ordenada_al_reves = sorted(cadena, reverse=True) # Ordena de mayor a menor
print(cadena_ordenada_al_reves) # ['y', 'u', 't', 't', 's', 'o', 'n', 'h', 'g', 'e', 'a', 'P', 'M', ' ', ' ']

# cadena.sort() -> Debería ordenar el str. No existe porque las cadenas son inmutables