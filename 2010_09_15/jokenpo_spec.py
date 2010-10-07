import unittest
from should_dsl import should, should_not, matcher
from jokenpo import jogo

class JokenpoTest(unittest.TestCase):
    def test_pedra_pedra(self):
        jogo("pedra","pedra") |should| equal_to ("empate")
    def test_pedra_tesoura(self):
        jogo("pedra","tesoura") |should| equal_to ("pedra")
    def test_pedra_papel(self):
        jogo("pedra","papel") |should| equal_to ("papel")
    def teste_tesoura_papel(self):
        jogo("tesoura","papel") |should| equal_to ("tesoura")
