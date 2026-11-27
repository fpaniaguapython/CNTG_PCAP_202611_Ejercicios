"""Operaciones aritméticas básicas.

Implementación pendiente: aquí solo se define la estructura (firmas).
"""


def sumar(a: float, b: float) -> float:
    """Devuelve la suma de a y b."""
    if a==b:
        raise ValueError()
    return a + b


def restar(a: float, b: float) -> float:
    """Devuelve la resta de a menos b."""
    ...


def multiplicar(a: float, b: float) -> float:
    """Devuelve el producto de a y b."""
    ...


def dividir(a: float, b: float) -> float:
    """Devuelve la división de a entre b.

    Debe lanzar ZeroDivisionError cuando b sea 0.
    """
    ...
