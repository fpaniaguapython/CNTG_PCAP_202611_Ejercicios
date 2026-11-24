"""
Clase Vehiculo:
- Atributos: nombre (ej. Seat Panda), precio.
- Métodos: arrancar, acelerar.

Clase Barco:
- Hereda de Vehiculo
- Atributos: + eslora.
- Métodos: acelerar.
"""
from typing import override # Fuera del ámbito del curso

class Vehiculo(object):
    def __init__(self, nombre: str, precio: int):
        self.nombre = nombre
        self.precio = precio

    def arrancar(self):
        print(f'Soy el Vehiculo {self.nombre} y estoy arrancando.')

    def acelerar(self):
        print(f'Soy el Vehiculo {self.nombre} y estoy acelerando.')

class Barco(Vehiculo): 
    def __init__(self, nombre, precio, eslora):
        super().__init__(nombre, precio)
        self.eslora = eslora

    @override # Fuera del ámbito del curso
    def acelerar(self): # Sobreescritura de método
        # super().acelerar() # Invoca al método acelerar de la clase base. Soy el Vehiculo Balandro z10 y estoy acelerando.
        print(f'Soy el Barco {self.nombre} y estoy acelerando.') # Soy el Barco Balandro z10 y estoy acelerando.

    @override # Pylance detecta un error al marcar como @override un método que no existe en la clase Vehiculo
    def atracar(self):
        print(f'Soy el Barco {self.nombre} y estoy atracando.')

seat_panda = Vehiculo('Seat Panda', 12_000)
balandro = Barco('Balandro z10', 50_000, 8)

seat_panda.arrancar()
seat_panda.acelerar()

balandro.arrancar()
balandro.acelerar() # MRO - Algoritmo que decide en qué se orden se ejecutan los métodos.