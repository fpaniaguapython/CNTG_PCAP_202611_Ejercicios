def crear_validador(longitud_minima):
    def validar(password):
        return len(password) >= longitud_minima
    return validar

validar_normal = crear_validador(8)
validar_seguro = crear_validador(12)

print(validar_normal("hola123"))       # False
print(validar_seguro("hola123456789")) # True