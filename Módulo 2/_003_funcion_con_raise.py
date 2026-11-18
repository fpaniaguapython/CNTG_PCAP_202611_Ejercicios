def sumar(numero_1: int, numero_2: int) -> int:
   """Suma dos números enteros.

    Params:
    - numero_1. Primer número.
    - numero_2. Segundo número.

    Return:
    - Resultado de la suma

    Exceptions:
    - TypeError. Se lanza cuando los tipos de los argumentos no son int.
   """
   if not isinstance(numero_1, int):
      raise TypeError('El tipo del primer argumento no es int')
   if not isinstance(numero_2, int):
      raise TypeError('El tipo del segundo argumento no es int')
   return numero_1+numero_2


numero_1 = '10'
numero_2 = 20
try:
    resultado = sumar()
    print(resultado)
except TypeError as te:
   print('Los tipos de las variables deben ser int')