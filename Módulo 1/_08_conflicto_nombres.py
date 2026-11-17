#import math # las referencias a pi incluyen el espacio de nombres (módulo) --> math.pi
from math import pi # Esta importación de la entidad pi es 'arriesgada'

pi = 18000 # Esta asignación podría ocurrir
# math.pi = 18000 # Esta asignación es poco probable que se nos ocurra

def circle_area(radius: float) -> float:
    """Return the area of a circle with the given radius."""
    return pi * radius ** 2

print(circle_area(10)) # 1800000 pero debería ser 314.1592653589793