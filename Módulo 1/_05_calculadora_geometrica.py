""" Módulo que contiene las funciones geométricas de cálculo de áreas.
- Área de un cuadrado
- Área de un rectángulo
- Área de un triángulo
- Área de un círculo

¡INCLUIMOS UNA EJECUCIÓN DE CÁLCULO DE ÁREA DEL CUADRADO
QUE SOLO SE EJECUTA SI EL MÓDULO ES EL PRINCIPAL! (EN CALCULADORA GEOMÉTRICA)
"""
import math

def square_area(side: float) -> float:
    """Return the area of a square with the given side length."""
    return side**2

def rectangle_area(base: float, height: float) -> float:
    """Return the area of a rectangle with the given base and height."""
    return base * height

def triangle_area(base: float, height: float) -> float:
    """Return the area of a triangle with the given base and height."""
    return (base * height) / 2

def circle_area(radius: float) -> float:
    """Return the area of a circle with the given radius."""
    return math.pi * radius ** 2

if __name__=='__main__':
    radio = 8.3
    area = circle_area(radio)
    print(f'El área del círculo con radio {radio} es {area}') # f-string