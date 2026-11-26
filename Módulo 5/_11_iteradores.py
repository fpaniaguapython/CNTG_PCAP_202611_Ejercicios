# Esta implementación del Iterador no entra en este programa de certificación

class JugueteHumanoide:
    def __init__(self, piezas: tuple):
        self._indice_pieza = 0
        self.piezas = piezas

    def __iter__(self):
        return self

    def __next__(self):
        if self._indice_pieza==len(self.piezas):
            self._indice_pieza=0
            raise StopIteration()
        pieza = self.piezas[self._indice_pieza]
        self._indice_pieza+=1
        return pieza

german = JugueteHumanoide(('Cabeza','Tronco','Brazo izquierdo', 'Brazo derecho'))

for trozo in german:
    print(trozo)