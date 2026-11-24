# Crear las siguientes clases:
# Clase Metralleta -> contiene el método disparar.
# Clase Radar -> Contiene el método detectar
# Clase Motor -> Contiene el método avanzar

# Utilizando herencia múltiple, vamos a construir una caja de cartón
# (clase CajaCarton) en un vehiculo de guerra.
# Atributos: ancho y alto.

# Instanciar una caja de cartón y hacerle avanzar, detectar con el radar
# a los enemigos o disparar ráfagas con la metralleta.

class Metralleta:
    def disparar(self):
        print('Disparando...')

class Radar:
    def detectar(self):
        print('Detectando...')

class Motor:
    def avanzar(self):
        print('Avanzando...')

class CajaCarton(Motor, Radar, Metralleta):
    def __init__(self, ancho, alto, largo):
        self.ancho = ancho
        self.alto = alto
        self.largo = largo

caja_mediana = CajaCarton(ancho=30, alto=20, largo=20)
caja_mediana.avanzar()
caja_mediana.detectar()
caja_mediana.disparar()