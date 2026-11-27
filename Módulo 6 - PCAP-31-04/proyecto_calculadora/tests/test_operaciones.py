import unittest

from calculadora import dividir, multiplicar, restar, sumar


class TestOperaciones(unittest.TestCase):

    def test_sumar_numeros_positivos(self):
        self.assertEqual(sumar(2, 3), 5) 

    def test_sumar_numeros_negativos(self):
        self.assertEqual(sumar(-5, -3), -8)

    def test_sumar_decimales(self):
        self.assertAlmostEqual(sumar(1.5, 2.25), 3.75)

    def test_sumar_con_cero(self):
        self.assertEqual(sumar(7, 0), 7)

    def test_sumar_numeros_iguales(self):
        with self.assertRaises(ValueError):
            sumar(10, 10)

if __name__ == "__main__":
    unittest.main()
