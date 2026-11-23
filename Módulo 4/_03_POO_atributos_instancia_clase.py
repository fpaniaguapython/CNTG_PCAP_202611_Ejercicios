class Trabajador:
    # Atributos de clase
    edad_jubilacion = 67
    def __init__(self, nombre, nss, fecha_contratacion):
        self.nombre = nombre # Atributos de instancia
        self.nss = nss # Atributos de instancia
        self.fecha_contratacion = fecha_contratacion # Atributos de instancia

    def set_salario(self, salario):
        self.salario = salario # Creando un nuevo atributo de instancia

elizabeth = Trabajador('Elizabeth', '3838427ABC', '2026/11/20')
deo = Trabajador('Deo', '34837829MNZ', '2025/05/03')
# Acceso al atributo de instancia
print(elizabeth.fecha_contratacion) # 2026/11/20
print(deo.fecha_contratacion) # 2025/05/03

# Acceso de lectura al atributo de clase
print(Trabajador.edad_jubilacion) # 67 - Acceso a través de la clase CORRECTO
print(elizabeth.edad_jubilacion) # 67 - Acceso a través de la instancia NO RECOMENDADO
print(deo.edad_jubilacion) # 67 - Acceso a través de la instancia NO RECOMENDADO

# Acceso de modificación al atributo de clase
Trabajador.edad_jubilacion=68 # Modificamos el valor para todas las instancias
print(Trabajador.edad_jubilacion) # 68
print(elizabeth.edad_jubilacion) # 68
print(deo.edad_jubilacion) # 68

print('***** OJO, NO HACER *****')
elizabeth.edad_jubilacion = 65 # PELIGRO - CREANDO UNA VARIABLE DE INSTANCIA
print(Trabajador.edad_jubilacion) # 68
print(elizabeth.edad_jubilacion) # 65
print(deo.edad_jubilacion) # 68

# Se pueden crear atributos de instancia en tiempo de ejecución
elizabeth.salario = 50_000 # Crea un atributo nuevo asociado SOLO al objeto elizabeth