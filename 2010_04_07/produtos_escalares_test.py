import unittest
from produto_escalar import multiplica_vetores, ListasComTamanhosDiferentes

class ProdutosEscalaresDeVetores(unittest.TestCase):
    def test_vetor_de_1x1(self):
        resultado = multiplica_vetores([1], [2])
        self.assertEquals(2, resultado)

    def test_outro_vetor_1x1(self):
        resultado = multiplica_vetores([3],[4])
        self.assertEquals(12, resultado)

    def teste_vetor_de_2x2(self):
        resultado = multiplica_vetores([1,2],[3,4])
        self.assertEquals(11, resultado)

    def teste_vetor_de_5x5(self):
        resultado = multiplica_vetores([1,1,1,1,1],[1,1,1,1,1])
        self.assertEquals(5, resultado)

    def teste_vetor_de_1x2(self):
        self.assertRaises(ListasComTamanhosDiferentes, multiplica_vetores, [1],[1,2] )

    def teste_vetor_de_2x1(self):
        self.assertRaises(ListasComTamanhosDiferentes, multiplica_vetores, [1,2],[1] )


if __name__ == '__main__':
    unittest.main()

