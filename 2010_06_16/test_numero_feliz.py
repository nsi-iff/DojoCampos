from numero_feliz import Numero
import unittest
from should_dsl import should, should_not

class TestNumero(unittest.TestCase):
    def test_felicidade_de_um(self):
        Numero(1) |should| be_feliz
    def test_felicidade_de_dois(self):
        Numero(2) |should_not| be_feliz
    def test_felicidade_de_treze(self):
        Numero(13) |should| be_feliz
    def test_felicidade_de_sete(self):
        Numero(7) |should| be_feliz
    def test_felicidade_de_noventa_e_sete(self):
        Numero(97) |should| be_feliz
    def test_felicidade_de_quatrocentos_e_noventa_e_seis(self):
        Numero(496) |should| be_feliz

if __name__ == '__main__':
    unittest.main()
