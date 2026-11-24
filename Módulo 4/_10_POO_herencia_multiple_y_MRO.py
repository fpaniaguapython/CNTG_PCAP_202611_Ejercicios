# Esta jerarquía provoca un error de tipo MRO
# debido a que D hereda de A por dos caminos: directamente por la izquierda
# e indirectamente por la derecha.

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(A, C): # TypeError: Cannot create a consistent method resolution order (MRO) for bases A, C
    pass


