"""Basic arithmetic operations."""

print(f'Cargando _03_calculadora.py... en el módulo con el __name__ {__name__} ')

def add(number_1: int, number_2: int) -> int:
    """Return the sum of two numbers."""
    return number_1 + number_2


def subtract(number_1: int, number_2: int) -> int:
    """Return the difference between two numbers."""
    return number_1 - number_2


def multiply(factor_1: int, factor_2: int) -> int:
    """Return the product of two numbers."""
    return factor_1 * factor_2


def divide(dividend: int, divisor: int) -> float:
    """Divide the dividend by the divisor, or raise an ZeroDivisionError if divisor is zero."""
    return dividend / divisor


if __name__=='__main__':
    print('Soy el principal')