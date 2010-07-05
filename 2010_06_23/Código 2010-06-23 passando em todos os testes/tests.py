import unittest
from romanroullete import RomanRoullete

class RomanRoulleteTestCase(unittest.TestCase):
   
    def test_validar_numero_pessoas(self):
        roleta = RomanRoullete(5, 0)
        self.assertEquals(len(roleta.lista_de_pessoas), 5)

    def test_duas_pessoas_passo_dois(self):
        intervalo_para_matar = 2      
        roleta = RomanRoullete(2, intervalo_para_matar)
        self.assertEquals(roleta.executar_pessoas(), 0)        

    def test_tres_pessoas_passo_tres(self):
        intervalo_para_matar = 3
        roleta= RomanRoullete(3, intervalo_para_matar)
        self.assertEquals(roleta.executar_pessoas(),1)

    def test_quatro_pessoas_passo_dois(self):
        intervalo_para_matar = 2
        roleta= RomanRoullete(4, intervalo_para_matar)
        self.assertEquals(roleta.executar_pessoas(),0)

    def test_quatro_pessoas_passo_tres(self):
        intervalo_para_matar = 3
        roleta= RomanRoullete(4, intervalo_para_matar)
        self.assertEquals(roleta.executar_pessoas(),0)

    def test_tres_pessoas_passo_dois(self):
        intervalo_para_matar = 2
        roleta = RomanRoullete(3, intervalo_para_matar)
        self.assertEquals(roleta.executar_pessoas(), 2) 
        
if __name__ == "__main__":
    unittest.main()

