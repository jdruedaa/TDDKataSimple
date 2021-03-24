from unittest import TestCase

from Procesador import Procesador


class ProcesadorTest(TestCase):
    def test_contar(self):
        self.assertEqual(Procesador().contar(""), [], "Cadena Vacía")
    def test_minimo(self):
        self.assertEqual(Procesador().minimo(""), [], "Cadena Vacía")
    def test_maximo(self):
        self.assertEqual(Procesador().maximo(""), [], "Cadena Vacía")
    def test_promedio(self):
        self.assertEqual(Procesador().promedio(""), [], "Cadena Vacía")

