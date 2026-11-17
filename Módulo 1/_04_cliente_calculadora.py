# import _03_calculadora # Opción 1 (nombre original)
import _03_calculadora as calc # Opción 2 (alias)
# from _03_calculadora import add, subtract # Opción 3 (importación de entidades)
# from _03_calculadora import * # Opción 4 (NO USAR - importa todas las entidades)
# from _03_calculadora import add as sumar # Opción 5 (importar una entidad y asignar un alias)

numero_1 = 10
numero_2 = 20

# resultado_suma = _03_calculadora.add(number_1=numero_1, number_2=numero_2) # Opción 1
resultado_suma = calc.add(number_1=numero_1, number_2=numero_2) # Opción 2
# resultado_suma = add(number_1=numero_1, number_2=numero_2) # Opción 3

print(resultado_suma)
