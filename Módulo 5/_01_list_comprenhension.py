##############################################
# COMPRENSIÓN DE LISTAS
##############################################

dias_semana = ['Luns', 'Martes', 'Mércores', 'Xoves', 'Venres', 'Sábado', 'Domingo']

# Comprensión de listas -> Los días de la semana convertidos a mayúsculas
dias_mayusculas = [dia.upper() for dia in dias_semana] # ['LUNS', 'MARTES', 'MÉRCORES', 'XOVES', 'VENRES', 'SÁBADO', 'DOMINGO']
print(dias_mayusculas)

# Comprensión de listas -> Los días de la semana convertidos a minúsculas
dias_minusculas = [dia.lower() for dia in dias_semana] # ['luns', 'martes', 'mércores', 'xoves', 'venres', 'sábado', 'domingo']
print(dias_minusculas)

# Comprensión de listas -> El número de caracteres de cada día de la semana
numero_caracteres = [len(dia) for dia in dias_semana] # [4, 6, 8, 5, 6, 6, 7]
print(numero_caracteres)

# Sustituir los espacios en blanco por _
titulos = ('El replandor', 'La ballena', 'Memorías de África', 'El nombre de la rosa')
lista_titulos_sin_espacio = [titulo.replace(' ', '_') for titulo in titulos]
print(lista_titulos_sin_espacio) # ['El_replandor', 'La_ballena', 'Memorías_de_África', 'El_nombre_de_la_rosa']

# Redondear a dos decimales una lista de números
numeros = [
    3.14159, 2.71828, 1.41421, 9.87654, 5.43210
]

# round(numero, numero_decimales)
# Redondear la lista a dos decimales

numeros_redondeados = [round(numero, 2) for numero in numeros]
print(numeros_redondeados) # [3.14, 2.72, 1.41, 9.88, 5.43]

# Conversión a cadena sustituyendo . por ,
# redondito = [ str(n2).replace(".", ",")  for n2 in (round(n1, 2) for n1 in numeros) ]
# print(redondito) # ['3,14', '2,72', '1,41', '9,88', '5,43']

# Usamos word2number_es
# pip install word2number_es

from word2number_es import w2n

def conversion_a_float(cadena):
    if cadena is None:
        return 0.0
    try:
        numero = float(cadena)
        return numero
    except:
        try:
            return float(w2n.word_to_num(cadena))
        except:
            return 0.0

datos = ('10.3', '8.4', '10', 'Tres', 'Mil quinientos', None)

datos_float = [conversion_a_float(dato) for dato in datos]
print(datos_float)# [10.3, 8.4, 10.0, 0.0, 0.0, 0.0] (Sin utilizar w2n.word_to_num)
print(datos_float)# [10.3, 8.4, 10.0, 3.0, 1500.0, 0.0] (Utilizando w2n.word_to_num)

##############################################
# COMPRENSIÓN DE LISTAS CON IF
##############################################

# Generar una lista con los números > 1000
numeros = [2000, 100, -8, 4000, 3000]
numeros_mayores_1000 = [numero for numero in numeros if numero>1000]
print(numeros_mayores_1000) # [2000, 4000, 3000]

# Obtener las facturas cuyo importe sea > 10000
class Factura:
    def __init__(self, numero_factura, importe):
        self.numero_factura = numero_factura
        self.importe = importe

    def __repr__(self):
        return str(self.__dict__)

f1 = Factura('001', 50_000)
f2 = Factura('002', 30_000)
f3 = Factura('003', 1_500)
facturas = [f1, f2, f3]

facturas_elevadas = [factura for factura in facturas if factura.importe>10_000]
print(facturas_elevadas)

##############################################
# COMPRENSIÓN DE LISTAS CON IF-ELSE
##############################################

# Obtener una lista con los valores ALTA o BAJA en función del importe > 10000
tipo_factura = ['ALTA' if factura.importe>10_000 else 'BAJA' for factura in facturas]
print(tipo_factura) # ['ALTA', 'ALTA', 'BAJA']

