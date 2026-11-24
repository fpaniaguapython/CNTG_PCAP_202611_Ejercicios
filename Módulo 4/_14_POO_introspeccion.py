class Enemigo:
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud

    def recibir_danyo(self, danyo):
        self.salud-=danyo
        print(f'El objeto {self.nombre} ha recibido una daño de {danyo}')

darth_vader = Enemigo('Darth Vader', 100)

print(type(darth_vader)) # <class '__main__.Enemigo'>

print(dir(darth_vader)) # ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', 'nombre', 'recibir_danyo', 'salud']
if 'salud' in dir(darth_vader):
    print('Tiene el atributo salud')
    if callable(darth_vader.salud):
        print('salud es una función')
    else:
        print('salud es un atributo')

print(hasattr(darth_vader, 'nombre')) # True
print(hasattr(darth_vader, 'recibir_danyo')) # True, aunque sea un método

el_nombre = getattr(darth_vader, 'nombre')
print(el_nombre) # Darth Vader

print(Enemigo.__class__) # {'__module__': '__main__', '__firstlineno__': 1, '__init__': <function Enemigo.__init__ at 0x000001A8E6957CC0>, 'recibir_danyo': <function Enemigo.recibir_danyo at 0x000001A8E6957D70>, '__static_attributes__': ('nombre', 'salud'), '__dict__': <attribute '__dict__'>, '__weakref__': <attribute '__weakref__'>, '__doc__': None}
print(darth_vader.__class__) # <class '__main__.Enemigo'>

print(Enemigo.__dict__) # <class 'type'>
print(darth_vader.__dict__) # {'nombre': 'Darth Vader', 'salud': 100}

print(Enemigo.__name__) # Enemigo
# print(darth_vader.__name__) # No existe. __name__ es propio de las clases

print(Enemigo.__module__) # __main__
print(darth_vader.__module__) # __main__

print(Enemigo.__bases__) # (<class 'object'>,)
#print(darth_vader.__bases__) # No existe. __main__ es propio de las clases