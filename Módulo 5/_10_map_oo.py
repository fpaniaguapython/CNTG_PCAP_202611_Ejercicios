def guardar(cliente):
    with open(cliente.nombre+'.dat', mode='w', encoding='utf-8') as fichero:
        fichero.write(str(cliente.__dict__))

class Cliente:
    def __init__(self, nombre, deuda):
        self.nombre = nombre
        self.deuda = deuda

cliente_1 = Cliente('Rambo', 10_000)    
cliente_2 = Cliente('Conan', 40_000)    
cliente_3 = Cliente('Batman', 5_000)

clientes = (cliente_1, cliente_2, cliente_3)

guardados = map(guardar, clientes)

for guardado in guardados:
    print('Guardando...')