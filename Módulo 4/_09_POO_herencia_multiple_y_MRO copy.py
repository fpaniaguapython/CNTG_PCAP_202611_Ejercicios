class A:
    def saludar(self):
        print('Hola, soy A')
    def despedir(self):
        print('Adios, soy A')
    def gritar(self):
        print('AAAAAAAAAAAAAA, soy A')
    def saltar(self):
        print('Soy A y estoy saltando')

class B(A):
    def saludar(self):
        print('Hola, soy B')
    def despedir(self):
            print('Adios, soy B')

class C(A):
    def saludar(self):
        print('Hola, soy C')
    def despedir(self):
            print('Adios, soy C')
    def gritar(self):
        print('AAAAAAAAAAAAAA, soy C')

class D(B,C):# Herencia múltiple
    def saludar(self):
        print('Hola, soy D')


objeto = D()
objeto.saludar() # Hola, soy D
objeto.despedir() # Adios, soy B (es la primera empezando por la izquierda)
objeto.gritar() # AAAAAAAAAAAAAA, soy C
objeto.saltar() # Soy A y estoy saltando (solo se ejecuta una vez)

