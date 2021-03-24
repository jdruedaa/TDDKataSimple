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

    def test_contarunnumero(self):
        self.assertEqual(Procesador().contar("1"), [1], "Cadena 1")

    def test_minimounnumero(self):
        self.assertEqual(Procesador().minimo("1"), [1,1], "Cadena 1")

    def test_maximounnumero(self):
        self.assertEqual(Procesador().maximo("1"), [1,1,1], "Cadena 1")

    def test_promediounnumero(self):
        self.assertEqual(Procesador().promedio("1"), [1,1,1,1], "Cadena 1")




