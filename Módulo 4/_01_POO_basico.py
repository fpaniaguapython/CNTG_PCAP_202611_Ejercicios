# Clase 
class Automovil:
    def __init__(self, marca, modelo, matricula): # Inicializador o constructor
        # Atributos de instancias
        self.marca = marca # self.marca es un atributo
        self.modelo = modelo # self.modelo es un atributo
        self.matricula = matricula # self.matricula es un atribuo
        self._arrancado = False # _ indica que el atributo es privado
        self.__rpm = 0 # __rpm se sustituye _Automovil__rpm

    # Métodos (de instancia)
    def arrancar(self):
        self._arrancado = True

    def detener(self):
        self.__rpm = 0
        self._arrancado = False

    def acelerar(self, cantidad=10):
        if self._arrancado==False:
            self.arrancar() # Invocación a un método del mismo objeto
        #self.__rpm = self.__rpm + cantidad # La línea siguente es equivalente a esta
        self.__rpm+=cantidad
    
    def desacelerar(self, cantidad=10):
        # self.__rpm = self.__rpm - cantidad # La línea siguente es equivalente a esta
        self.__rpm-=cantidad

    # Método de acceso de lectura (get)
    def get_rpm(self):
        return self.__rpm

    # Método de acceso de modificación (set)
    def set_rpm(self, nuevo_rpm):
        self.__rpm = nuevo_rpm

# Instanciación o creación del objeto o instancia
auto_fernando = Automovil(marca='Kia', modelo='Ceed', matricula='M-7786-HH')
auto_pablo = Automovil(marca='BMW', modelo='Z5', matricula='CC-1223-Z')

# Acceso a los atributos del objeto
print(auto_pablo.marca)
auto_pablo.marca = 'Fiat'

# Utilizador los métodos para realizar acciones sobre el objeto
auto_pablo.arrancar()
auto_pablo.acelerar(cantidad=100)
auto_pablo.acelerar(cantidad=10)
auto_pablo.acelerar(cantidad=120)
# print(auto_pablo.__rpm) # NO FUNCIONA, porque rpm se renombra
# print(auto_pablo._Automovil__rpm) # NO SE DEBE HACER
auto_pablo.get_rpm() # ESTAMOS ACCEDIENDO A UN ATRIBUTO ENCAPSULADO

auto_pablo.detener()
# auto_pablo.__rpm = 4_000 # NO FUNCIONA, porque rpm se renombra
# auto_pablo._Automovil__rpm = 4_000 # NO SE DEBE HACER