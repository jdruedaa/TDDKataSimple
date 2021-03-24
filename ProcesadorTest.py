from unittest import TestCase

from Procesador import Procesador


class ProcesadorTest(TestCase):
    def test_contar(self):
        self.assertEqual(Procesador().contar(""), [0,0,0,0], "Cadena Vacía")

