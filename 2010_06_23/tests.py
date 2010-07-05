import unittest
from romanroullete import RomanRoullete

class RomanRoulleteTestCase(unittest.TestCase):


    def test_validar_numero_pessoas(self):
        roleta = RomanRoullete(5, 0)
        self.assertEquals(len(roleta.lista_de_pessoas), 5)

    def test_duas_pessoas_passo_dois(self):
        matar = 2      
        roleta = RomanRoullete(2, matar)
        self.assertEquals(roleta.executar_pessoas(), 1)

    def test_tres_pessoas_passo_dois(self):
        matar = 2
        roleta = RomanRoullete(3, matar)
        self.assertEquals(roleta.executar_pessoas(), 3) 

    def test_tres_pessoas_passo_tres(self):
        matar = 3
        roleta= RomanRoullete(3, matar)
        self.assertEquals(roleta.executar_pessoas(),2)

if __name__ == "__main__":
    unittest.main()
