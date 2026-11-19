"""
Crear una función que escriba en un fichero los datos de una película.
Los argumentos de la función son:
- Título
- Director
- Año de estreno

Verificar que el tipo del año es int --> TypeError
Verificar que el valor del año es igual o inferior al año actual --> YearError

Nota: YearError no existe. Hay que crear la clase y buscar la clase del árbol
de excepciones que mejor encaje.
"""
from datetime import datetime

class YearError(ValueError):
    pass

def guardar_pelicula(titulo: str, director: str, anyo_estreno: int):
    if not isinstance(anyo_estreno, int):
        raise TypeError('El año debe ser un número entero')
    anyo_actual = datetime.now().year
    if anyo_estreno>anyo_actual:
        raise YearError('El año de estreno no puede ser superior al año actual')
    with open('peliculas.txt', mode='at', encoding='utf-8') as fichero:
        fichero.write(f'Título:{titulo}. Director:{director}. Año:{anyo_estreno}\n')

titulo = input('Título:')
director = input('Director:')
anyo_estreno = int(input('Año de estreno:'))
try:
    guardar_pelicula(titulo, director, anyo_estreno)
except TypeError:
    print('El año de estreno debe ser un número entero')
except YearError:
    print('El año de estreno no puede ser posterior al año actual')
except Exception:
    print('Ha ocurrido una excepción no controlada. Contacte con el adminitrador.')