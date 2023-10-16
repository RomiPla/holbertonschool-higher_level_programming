#!/usr/bin/python3
"""
==================================
Test de 6-max_integer_test.py
==================================
"""

"""
   Esto es un test para la funcion max_integer
   primero importamos el modulo 6-max_integer_test.py,
   de este modulo traemos la funcion max_integer
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """TestMax Integer es un testing class
     para la funcion max_integer"""

    def test_max(self):
        """ testea una lista, la
        funcion debe obtener el max int"""
        self.assertEqual(max_integer([1, 6, 10, 24, 758, 4, 3, 1]), 758)

    def test_max_iguales(self):
        """testea una lista donde
        todos los int son iguales"""
        self.assertEqual(max_integer([6, 6, 6, 6, 6]), 6)

    def test_max(self):
        """ testea una lista
        donde hay numeros negativos"""
        self.assertEqual(max_integer([-1, -6, 10, -24, -758, 4, -3, 1]), 10)

    def test_max_none(self):
        """testea una
        lista vacia"""
        self.assertEqual(max_integer([]), None)

    def test_max_error(self):
        """testea error
        por tipo de datos
        incorrectos"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, 3, 'Hola'])
