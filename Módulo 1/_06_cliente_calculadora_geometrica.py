import _05_calculadora_geometrica as calculadora_geometrica

base_rectangulo = float(input('Introduce la base del rectángulo:'))
altura_rectangulo = float(input('Introduce la altura del rectándulo:'))
unidad = input('Introduce la unidad utilizada:')

# Argumentos posicionales
area_1 = calculadora_geometrica.rectangle_area(base_rectangulo, altura_rectangulo)
# Argumentos keywords
area_2 = calculadora_geometrica.rectangle_area(base=base_rectangulo, height=altura_rectangulo)

print(f'El área del rectángulo con base {base_rectangulo} y altura {altura_rectangulo} es {area_1} {unidad}')
print(f'El área del rectángulo con base {base_rectangulo} y altura {altura_rectangulo} es {area_2} {unidad}')