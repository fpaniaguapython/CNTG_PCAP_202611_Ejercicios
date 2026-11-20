# FORMATO ES DDMMYYYYHHMM 
# TIPO INCIDENCIA (5 CARACTERES) 
# ID DE CLIENTE HASTA EL FINAL
registro_01 = "201120261722GRAVEOR1221"
registro_02 = "201120261722MEDIALU4432"
registro_03 = "201120261722LEVE CO134412"
registros = [registro_01, registro_02, registro_03]

# Separar las partes de las cadenas y las muestre por pantalla
# Dia: 20
# Mes: 11
# Año: 2026
# HORA: 17:22
# CRITICIDAD: GRAVE
# ID CLIENTE: CO134412

def get_datos(registro: str) -> tuple:
    dia = int(registro[:2])
    mes = int(registro[2:4])
    año = int(registro[4:8])
    hora = int(registro[8:10])
    minuto = int(registro[10:12])
    critidad = registro[12:17].strip() # Elimina el espacio final si lo hay
    id_cliente = registro[17:].strip() # Eliminar el salto de línea posible
    resultado = (dia, mes, año, hora, minuto, critidad, id_cliente)
    return resultado

def mostrar_datos(datos):
    print(f'Fecha:{datos[0]}/{datos[1]}/{datos[2]}')
    print(f'Hora:{datos[3]}:{datos[4]}')
    print(f'Criticidad:{datos[5]}')
    print(f'Cliente:{datos[6]}')

for registro in registros:
    datos = get_datos(registro=registro)
    mostrar_datos(datos) 