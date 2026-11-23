class Animal:
    def __init__(self, especie, nombre, fecha_nacimiento, posicion):
        self.especie = especie
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.posicion = posicion

    def comer(self):
        print(f'Soy {self.nombre } y estoy comiendo como animal')

    def reproducir(self):
        print(f'Soy {self.nombre} y me estoy reproduciendo como animal')

class AnimalDesplazable(Animal):
    def __init__(self, especie, nombre, fecha_nacimiento, posicion, velocidad):
        super().__init__(especie, nombre, fecha_nacimiento, posicion)
        self.velocidad = velocidad

    # Nuevo método incorporado a la clase derivada
    def mover(self, nueva_posicion):
         print(f'Soy {self.nombre} y me estoy moviendo como animal desplazable')

    # Sobreescritura de método (sustituir la versión original del método por otra)
    def reproducir(self):
            print(f'Soy {self.nombre} y me estoy reproduciendo como animal desplazable')

caracol = AnimalDesplazable('Caracol', 'Fred', '2025/01/01', 
                            posicion=(10, 5, 0), velocidad=1)

# caracol es simultáneamente objeto AnimalDesplazable y Animal - POLIMORFISMO
print(isinstance(caracol, AnimalDesplazable)) # True
print(isinstance(caracol, Animal)) # True

caracol.comer()
caracol.mover(nueva_posicion=(3,5,0))
caracol.reproducir()

coral = Animal('Coral', 'Zacarías', fecha_nacimiento='1988/01/05',
               posicion=(10,8,1))
coral.comer()
# coral.mover(nueva_posicion=(9,9,0) # Un Animal no sabe moverse
coral.reproducir()

