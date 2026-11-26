class Factura:
    _iva = 21
    def __init__(self, numero, proveedor, cliente, items):
        self.numero = numero
        self.proveedor = proveedor
        self.cliente = cliente
        self.items = items

    def pagar(self, numero):
        self.pagado = True
        self.numero = 0



f1 = Factura(10, 'p1', 'c1', ['pr1','pr2'])
f2 = Factura(20, 'p2', 'c2', ['pr3','pr3'])
f1.pasado_a_cobro = True
pass



    
    



    