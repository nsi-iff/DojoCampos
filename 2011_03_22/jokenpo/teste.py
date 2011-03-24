import unittest
from should_dsl import *
from jokenpo import jokenpo

class TestJokenpo(unittest.TestCase):
    def test_papel_empata_com_papel(self):
        jokenpo("papel","papel") |should| equal_to ("empate")
    
    def test_pedra_ganha_de_tesoura(self):
        jokenpo("pedra", "tesoura") |should| equal_to ("pedra")
    
    def test_tesoura_ganha_de_papel(self):
        jokenpo("tesoura", "papel") |should| equal_to ("tesoura")
    
    def test_papel_ganha_de_pedra(self):
        jokenpo("papel", "pedra") |should| equal_to ("papel")

    def test_pedra_empata_com_pedra(self):
        jokenpo("pedra", "pedra") |should| equal_to ("empate")
    def test_tesoura_perde_pedra(self):
        jokenpo("tesoura","pedra") |should| equal_to ("pedra")
 
if __name__ == "__main__":
    unittest.main()
    
