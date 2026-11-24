# Definir la clase Enemigo
# Atributos: nombre, salud
# Métodos: recibir_danyo, recuperar_salud

class Enemigo(object): # La herencia de object no se pone, está implícito
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud

    def recibir_danyo(self, danyo):
        self.salud-=danyo
        print(f'El objeto {self.nombre} ha recibido una daño de {danyo}')

    def recuperar_salud(self, cantidad_salud):
        self.salud+=cantidad_salud
        print(f'El objeto {self.nombre} ha incrementado su salud en {cantidad_salud}')

    def __str__(self) -> str:
        return str(self.__dict__)
        #return f'Nombre:{self.nombre}. Salud:{self.salud}'

    def __repr__(self) -> str:
        return '__repr__'

# Definir la clase EnemigoHostil
# Hereda de Enemigo
# Atributos: danyo (el que hace)
# Método: atacar

class EnemigoHostil(Enemigo):
    def __init__(self, nombre, salud, danyo):
        super().__init__(nombre, salud)
        self.danyo = danyo

    def atacar(self):
        print(f'El objeto {self.nombre} está atacando')

    def __str__(self) -> str:
        return str(self.__dict__)

# Crear una instancia de Enemigo
# Invocamos a sus métodos recibir_danyo y recuperar_salud

batman = Enemigo('Batman', 100)
batman.recibir_danyo(30)
batman.recuperar_salud(20)

print(batman) # Invoca a __str__

# Creamos una instancia de EnemigoHostil
# Invocamos a sus métodos recibir_danyo y recuperar_salud
# Invocamos a su método atacar

joker = EnemigoHostil('Joker', 100, 10)
joker.recibir_danyo(50)
joker.recuperar_salud(10)
joker.atacar()

print(joker)