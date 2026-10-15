import unittest
from ordenacao import ordenacao_insercao, ordenacao_intercalacao

class TestesOrdenacao(unittest.TestCase):
    def setUp(self):
        self.casos = {
            "vazia": [],
            "um_elemento": [42],
            "elementos_iguais": [7, 7, 7, 7, 7, 7],
            "ja_ordenada": [1, 2, 3, 4, 5, 6, 7, 8],
            "invertida": [8, 7, 6, 5, 4, 3, 2, 1],
            "aleatoria": [23, 1, 45, 12, 8, 99, 3, 12, 5]
        }

    def test_ordenacao_insercao(self):
        for nome, lista in self.casos.items():
            with self.subTest(caso=nome):
                resultado, _ = ordenacao_insercao(lista)
                self.assertEqual(resultado, sorted(lista))

    def test_ordenacao_intercalacao(self):
        for nome, lista in self.casos.items():
            with self.subTest(caso=nome):
                resultado, _ = ordenacao_intercalacao(lista)
                self.assertEqual(resultado, sorted(lista))

if __name__ == "__main__":
    unittest.main()
