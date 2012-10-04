import unittest
from should_dsl import should
from fator_primo import fatorPrimo

class TestFatorPrimo(unittest.TestCase):

    def teste_0_nao_eh_primo(self):
        fatorPrimo(0) |should| equal_to(False)

    def teste_1_nao_eh_primo(self):
        fatorPrimo(1) |should| equal_to(False)
        
    def test_3_eh_primo(self):
        fatorPrimo(3) |should| equal_to(True)

    def test_4_nao_eh_primo(self):
        fatorPrimo(4) |should| equal_to(False)

    def teste_5_eh_primo(self):
        fatorPrimo(5) |should| equal_to(True)
        
    def teste_6_nao_eh_primo(self):
        fatorPrimo(6) |should| equal_to(False)
        
    def teste_35_nao_eh_primo(self):
        fatorPrimo(35) |should| equal_to(False)
