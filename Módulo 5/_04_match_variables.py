punto = (10, 20)
match punto:
    case (0, 0):
        print("Origen")
    case (x, y):
        print(f"Coordenadas: {x}, {y}") # Coordenadas: 10, 20

# Uso práctico de las variables
posicion = (10, 0)

match posicion:
    case (x, y) if y == 0:
        print("Está en el suelo")
    case (x, y) if x ==0:
        print("Está en la pared izquierda")
    case _:
        print("Está en algún sitio")


class Factura:
    def __init__(self, numero, importe, estado):
        self.numero = numero
        self.importe = importe
        self.estado = estado
    def pasar_a_cobro(self):
        print(f'Pasando a cobro la factura {self.numero}')
    def pasar_a_caja(self):
        print(f'Pasando a caja la factura {self.numero}')

factura_1 = Factura('001', 1000, 'Pendiente')
factura_2 = Factura('002', 2000, 'Cobrada')

facturas = [factura_1, factura_2]

for factura in facturas:
    match factura:
        case f if f.estado=='Pendiente':
            f.pasar_a_cobro()
        case f if f.estado=='Cobrada':
            f.pasar_a_caja()
    

